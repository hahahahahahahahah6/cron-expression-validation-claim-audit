import tempfile
import unittest
from pathlib import Path
from cron_expression_validation_claim_audit.audit import audit, claims, evidence, main
from cron_expression_validation_claim_audit.phrases import CRONEXPRESSIONVALIDATION, NOCRONEXPRESSIONVALIDATION, GENERIC_NAMES

class AuditTests(unittest.TestCase):
    def test_phrases(self):
        for phrase in CRONEXPRESSIONVALIDATION:
            with self.subTest(phrase=phrase): self.assertTrue(claims(phrase)[0])
        for phrase in NOCRONEXPRESSIONVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual((set(), {phrase}), claims(phrase))
        self.assertEqual((set(), set()), claims('```\nvalidate cron expression\n```'))

    def test_routes(self):
        cases = ['import croniter as ci\nci.croniter.is_valid(x)', 'from croniter import croniter as c\nc.is_valid(x)', 'from croniter.croniter import croniter as c\nc(x)', 'import croniter as ci\nci.croniter(x)', 'import crontab as ct\nct.CronSlices.is_valid(x)', 'from crontab import CronSlices as c\nc.is_valid(x)', 'import crontab as ct\nct.CronSlices(x)', 'from crontab import CronSlices as c\nc(x)', 'import cronex as cx\ncx.CronExpression(x)', 'from cronex import CronExpression as c\nc(x)']
        cases += ['obj.%s(x)' % n for n in GENERIC_NAMES]
        cases += ['from helpers import %s as f\nf(x)' % n for n in GENERIC_NAMES]
        for source in cases:
            with self.subTest(source=source): self.assertTrue(evidence(source))

    def test_non_evidence(self):
        cases = ['import croniter', 'import crontab', 'import cronex', 'import cron_validator', 'croniter(x)', 'CronExpression(x)', 'CronSlices(x)', 'is_valid(x)', 'validate(x)', 'obj.croniter(x)', 'obj.CronExpression(x)', 'obj.CronSlices(x)', 'obj.is_valid(x)', 'obj.validate(x)', 'croniter.get_next(x)', 'croniter.get_prev(x)', 'croniter.match(x)', 'croniter.match_range(x)', 'croniter.expand(x)', 'CronValidator.parse(x)', 'CronValidator.match_timestamp(x)', 'CronValidator.match_datetime(x)', 'CronValidator.get_execution_time(x)', 'cronex.parse_atom(x)', 'obj.check_trigger(x)', 'obj.is_valid', 'crontab.CronTab(x)', 're.match(x)', 're.search(x)', 're.fullmatch(x)', 'schedule.run(x)', 'apscheduler.add_job(x)', 'sched.enter(x)', 'validators.url(x)', 'validators.ipv4(x)', 'validators.ipv6(x)', 'validators.email(x)', 'validators.card_number(x)', 'validators.domain(x)', 'validators.uuid(x)', 'validators.mac_address(x)', 'urlparse(x)', 'urlsplit(x)', 'netaddr.IPAddress(x)', 'netaddr.EUI(x)', 'payment.charge(x)', 'extract(x)', '"validate cron expression"', 'x.validate_cron_expression', 'x =', 'subprocess.run(["validate cron expression"])', 'from croniter import croniter\ncroniter = 1\ncroniter(x)', 'def validate_cron_expression(x): pass\nobj.validate_cron_expression(x)', 'import croniter as c\nwith thing() as c: pass\nc.croniter(x)']
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_findings(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'README.md').write_text('validate cron expression')
            self.assertEqual('HIGH', audit(p)[0]['severity'])
            (p/'test_it.py').write_text('obj.validate_cron_expression(x)')
            self.assertEqual('MEDIUM', audit(p)[0]['severity'])
            self.assertEqual(0, main(['audit',d])); self.assertEqual(2, main(['audit',d,'--fail-on','medium']))
            (p/'app.py').write_text('obj.validate_cron_expression(x)')
            self.assertEqual([], audit(p))
            (p/'README.md').write_text('no cron expression validation')
            self.assertEqual('documented-no-cron-expression-validation-claim-false', audit(p)[0]['id'])
            self.assertEqual([], audit(p, ['app.py']))

    def test_scanning(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'README.md').write_text('validate cron expression')
            for directory in ('docs', 'examples', 'fixtures'):
                (p/directory).mkdir(); (p/directory/'code.py').write_text('obj.cron_check(x)')
            self.assertEqual('HIGH', audit(p)[0]['severity'])
            (p/'a.py').write_text('from croniter import croniter'); (p/'b.py').write_text('croniter(x)')
            self.assertEqual('HIGH', audit(p)[0]['severity'])

    def test_self_audit(self):
        self.assertEqual([], audit(Path(__file__).resolve().parents[1]))

if __name__ == '__main__': unittest.main()
