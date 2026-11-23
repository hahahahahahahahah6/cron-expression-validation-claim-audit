# Schedule-string claim audit

This offline static auditor compares documentation with Python call shapes. It does not execute the inspected code. It reads the root README and Markdown files under docs, excluding fenced blocks, and examines Python source separately for production and test evidence. Findings are heuristic and require review.

## Usage

```sh
python3 -m cron_expression_validation_claim_audit --version
python3 -m cron_expression_validation_claim_audit audit .
python3 -m cron_expression_validation_claim_audit audit . --json --fail-on medium --ignore vendor
```

The console entry point is:

```
cron-expression-validation-claim-audit
```

The default threshold is high; medium includes test-only evidence. Repeat `--ignore` for multiple path prefixes. Exit codes are 0 for pass, 2 for findings at the threshold, and 1 for usage or I/O errors.

Finding identifiers:

```
documented-cron-expression-validation-claim-false
documented-no-cron-expression-validation-claim-false
```

## Differentiation

Generic input checks determine whether input is checked at all.

ISBN checks judge book-number check digits.

ISSN checks judge serial-number check digits.

IBAN checks judge bank account numbers.

UUID checks judge identifier strings.

Semantic version checks judge version strings.

MAC address checks judge hardware addresses.

Scheduled execution runs jobs rather than judging schedule strings.

Date checks judge calendar dates.

Timeouts limit execution duration.

Schedule description turns a string into human-readable text.

Payment processing takes a card payment.

Card extraction reads card details from documents.

Authentication can prove account ownership using codes or confirmation links.

Password verification compares a password with a stored hash.

Password hashing prepares a password for storage.

Password generation mints random passwords.

PDF encryption protects a file with a password.

Email sending delivers mail.

SMS sending delivers text messages.

Document extraction reads data from documents.

Barcode scanning decodes images.

Email checks judge address format or deliverability.

Phone checks judge number format or region.

Password strength checks judge password strength.

JSON Schema checks judge data against a schema.

Card checks judge number format, brand, and Luhn digits.

Domain checks judge host names.

URL checks judge web addresses.

IP checks judge numeric addresses.

JSON decoding produces a value.

Regular expressions match patterns.

URL parsing splits web addresses into parts.

Fetching retrieves a web address over a network.

DNS resolution looks up a name.

Barcode generation encodes account numbers.

Account-number extraction reads documents.

Next-run calculation uses a schedule.

Moment matching compares a time with a schedule.

Expansion produces field lists.

Parsing produces element objects.

A crontab file contains jobs and commands.

A single field is not an entire schedule string.

Schedule generation creates a new string.

The spreadsheet reading family is outside this tool.

The spreadsheet generation family is outside this tool.

The word-document reading family is outside this tool.

The word-document generation family is outside this tool.

The presentation reading family is outside this tool.

The presentation generation family is outside this tool.

The PDF extraction family is outside this tool.

The PDF generation family is outside this tool.

The PDF merging family is outside this tool.

The PDF splitting family is outside this tool.

The PDF rotation family is outside this tool.

The PDF form-filling family is outside this tool.

The PDF watermarking family is outside this tool.

The PDF redaction family is outside this tool.

The PDF compression family is outside this tool.

The PDF annotation family is outside this tool.

The table extraction family is outside this tool.

The OCR family is outside this tool.

The document extraction family is outside this tool.

The e-signature family is outside this tool.

The screen recording family is outside this tool.

The video generation family is outside this tool.

The QR code generation family is outside this tool.

The barcode generation family is outside this tool.

The barcode scanning family is outside this tool.

The audio mixing family is outside this tool.

The audio generation family is outside this tool.

The audio editing family is outside this tool.

The source separation family is outside this tool.

The speech recognition family is outside this tool.

The text-to-speech family is outside this tool.

The noise suppression family is outside this tool.

The music generation family is outside this tool.

The music transcription family is outside this tool.

## Limitations

```.text
validate cron expression
```

The bare phrase above is deliberately a claim phrase: in tool docs it almost always names checking whether a cron-expression string is well-formed. But the phrase can also name checking a schedule string against a bank of known-good schedules or a remote database, not by the tool's own code. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
check cron expression
```

The bare phrase above is deliberately a claim phrase: it almost always names a format judgement. But the phrase can also name a manual step in a runbook, not code. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron expression validation
```

The bare phrase above is deliberately a claim phrase: in tool docs it almost always names checking whether a cron-expression string is well-formed. But the phrase can also name a validation feature listed in a roadmap, not one the tool implements. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron expression validator
```

The bare phrase above is deliberately a claim phrase: it almost always names a tool that judges schedule strings. But the phrase can also name a hosted web page that checks a pasted schedule, not the tool's own code. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
valid cron expression
```

The bare phrase above is deliberately a claim phrase: it almost always names a cron-expression string that passed a check. But the phrase can also name advice to the reader, with no checking capability at all. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron expression is valid
```

The bare phrase above is deliberately a claim phrase: it almost always names the outcome of a check. But the phrase can also name the outcome of a lookup that succeeded, with no format check performed by the tool. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron expression string validation
```

The bare phrase above is deliberately a claim phrase: it almost always names a format judgement. But the phrase can also name a spec section with no checking code behind it. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
validate cron expression string
```

The bare phrase above is deliberately a claim phrase: it almost always names checking whether a cron-expression string is well-formed. But the phrase can also name checking a string against an allow-list, not judging its format. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
verify cron expression
```

The bare phrase above is deliberately a claim phrase: it almost always names checking whether a cron-expression string is well-formed. But the phrase can also name proving a schedule exists in a job list, not judging the string's format. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
detect invalid cron expression
```

The bare phrase above is deliberately a claim phrase: it almost always names finding a cron-expression string that fails a format check. But the phrase can also name finding a string that fails a length rule only, with no full format check involved. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron expression well formed
```

The bare phrase above is deliberately a claim phrase: it almost always names the outcome of a check. But the phrase can also name a theoretical discussion with no checking code behind it. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
is valid cron expression
```

The bare phrase above is deliberately a claim phrase: it almost always names the outcome of a check. But the phrase can also name a claim about a schedule the tool generated itself, with no judgement performed on input. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron expression format validation
```

The bare phrase above is deliberately a claim phrase: it almost always names a format judgement. But the phrase can also name checking only the spacing layout of a string, with no full format check involved. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
validate cron schedule
```

The bare phrase above is deliberately a claim phrase: it almost always names checking whether a schedule string is well-formed. But the phrase can also name checking that a schedule is set at all (presence), not judging the string's format. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron schedule validation
```

The bare phrase above is deliberately a claim phrase: it almost always names checking a schedule string. But the phrase can also name validating that jobs are scheduled at all, with no string judgement involved. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
check cron schedule
```

The bare phrase above is deliberately a claim phrase: it almost always names a format judgement on a schedule string. But the phrase can also name a manual step in a runbook, not code. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
valid cron schedule
```

The bare phrase above is deliberately a claim phrase: it almost always names a schedule string that passed a check. But the phrase can also name a schedule that runs, with no format check on the string behind it. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron check
```

The bare phrase above is deliberately a claim phrase: it almost always names a format judgement on a schedule string. But the phrase can also name a health check on the cron daemon or service, with no expression judgement involved at all. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
validate cron string
```

The bare phrase above is deliberately a claim phrase: it almost always names checking whether a cron string is well-formed. But the phrase can also name checking a string against an allow-list, not judging its format. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
validate cron value
```

The bare phrase above is deliberately a claim phrase: it almost always names checking whether a cron value is well-formed. But the phrase can also name checking that a config value exists at all, not judging its format. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
cron expression validation
```

The bare phrase above can also name a check performed by the platform that runs the schedule — an external scheduler rejecting a bad expression at deploy time — not by the tool's own code. A doc that means that is a false positive. The tool flags the phrase and leaves the judgement to a human.

```.text
validate cron tab
```

The phrase above is deliberately NOT in the phrase lists: a crontab is a file of jobs with commands, and judging a whole tab is the scheduled family's territory, not this family's.

A croniter construction is evidence even when the built iterator is only ever used to compute the next run: the construction itself performed the judgement at instantiation, and only the call shape is the fingerprint. That is a deliberate choice; the call shape is the fingerprint.

A lone croniter.get_next / get_prev call with no croniter construction in the same module is NOT evidence: computing a run time is scheduling use, and the judgement lives in the construction, which is absent. That is a deliberate choice; the call shape is the fingerprint.

A croniter.expand call is NOT evidence: expanding an expression into field lists is parsing, and the returned lists carry no validity verdict. That is a deliberate choice; the call shape is the fingerprint.

A CronValidator.parse call is NOT evidence: parsing an expression into element objects is parsing, and the raise is a parse failure, not a validity-judgement call. That is a deliberate choice; the call shape is the fingerprint.

A cronex parse_atom call is NOT evidence: parsing one field atom is not judging a whole expression string. That is a deliberate choice; the call shape is the fingerprint.

A cronex CronExpression.check_trigger call is NOT evidence: matching a datetime against an expression is a match check, not a validity judgement. That is a deliberate choice; the call shape is the fingerprint.

A CronSlice.is_valid read is NOT evidence: a CronSlice holds one field, not a whole expression string, and it is built from a field-definition dict, not from a string. That is a deliberate choice; the call shape is the fingerprint.

A crontab CronTab construction is NOT evidence: a whole crontab is a file of jobs with commands, and a malformed tab silently yields zero jobs — no judgement is performed at all. That is a deliberate choice; the call shape is the fingerprint.

A re.match call on a cron pattern alone is NOT evidence: matching a pattern accepts malformed strings and rejects well-formed ones, because a regex is not a validation call.

A .is_valid() call on a base that is not a croniter-class base or a CronSlices-class base is missed, even when the base holds a croniter object built in another module or through a helper the tracer cannot follow. The tool checks the call shape, not the value.

A bare import of a schedule-string judgement library with no call is not evidence, even when the import is the only thing the module does.

A doc that claims the checked capability in a roadmap, changelog, or TODO is still a claim: the tool reads prose, not intent.

A doc that denies the checked capability with a phrase outside the denial list (for example a paraphrase the list does not contain) is not recognised as a denial and the claim side still fires if a claim phrase is present.

A claim in a file that is not the root README.md and has no `docs` path component is not read at all (for example a claim in a top-level CHANGELOG.md is invisible to the tool).

Evidence split across two modules is not evidence: each route must sit in a single module, even when the two halves obviously belong together.

A route call on a name the module locally defines (a function, method, or class with the same name) is shadowed and does not count, even when the local definition is a thin wrapper around the real library call.

Dead code counts: a validation route in a function that is never called is still evidence, because the tool reads code, not execution.

A subprocess call that shells out to a cron validator (any cron validator CLI) is NOT evidence by design: a shell command name in a string literal is never evidence.

A single generic input check with no cron leg is not evidence, even when the checked input happens to be a cron-expression string: checking that input exists says nothing about its format, and this family covers schedule-string judgement only.

A single email validation call with no cron leg is not evidence, even when the validated address sits next to a cron-expression field: email addresses are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single phone number validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: phone numbers are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single URL validation call with no cron leg is not evidence, even when the validated address contains a cron-expression string: web addresses are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single IP address validation call with no cron leg is not evidence, even when the validated address sits next to a cron-expression field: numeric addresses are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single domain validation call with no cron leg is not evidence, even when the validated name sits next to a cron-expression field: host names are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single ISBN validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: book numbers are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single ISSN validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: serial numbers are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single IBAN validation call with no cron leg is not evidence, even when the validated number sits next to a cron-expression field: bank account numbers are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single UUID validation call with no cron leg is not evidence, even when the validated identifier sits next to a cron-expression field: identifiers are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single semver validation call with no cron leg is not evidence, even when the validated version sits next to a cron-expression field: version strings are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single MAC address validation call with no cron leg is not evidence, even when the validated address sits next to a cron-expression field: hardware addresses are a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A single extraction call with no cron leg is not evidence, even when the extracted data is a cron-expression string: reading data out of a document is a different capability, and this family covers checking whether a cron-expression string is well-formed only.

A generic name that a module locally defines is shadowed and does not count, even when the local definition validates cron expressions.

A generic name called through an alias chain the tracer cannot follow (for example a name imported under two successive aliases) is missed.

The tool matches exact phrases only, not meaning: a doc that paraphrases the capability without using any listed phrase is invisible to the claim side, and a doc that uses a listed phrase for a different capability is flagged anyway.

The tool reads Python source only: a validation implementation in another language in the same repo is invisible to the evidence side.

The tool never executes code and never touches the network: a validation route that only exists at runtime (a dynamically imported module, a plugin loaded by name) is invisible.

The following claims are NOT in the phrase lists: generic input validation claims, JSON field-name claims, email sending claims, SMS sending claims, phone number validation claims, email validation claims, password strength claims, authentication claims, JSON extraction claims, barcode scanning claims, QR code scanning claims, audio mixing claims, audio generation claims, audio editing claims, source separation claims, speech recognition claims, text-to-speech claims, noise suppression claims, music generation claims, music transcription claims, video editing claims, screen recording claims, video generation claims, QR code generation claims, barcode generation claims, spreadsheet reading claims, spreadsheet generation claims, word-document reading claims, word-document generation claims, presentation reading claims, presentation generation claims, PDF extraction claims, PDF generation claims, PDF merging claims, PDF splitting claims, PDF encryption claims, PDF rotation claims, PDF form-filling claims, PDF redaction claims, PDF compression claims, PDF annotation claims, table extraction claims, OCR claims, document extraction claims, e-signature claims, payment-processing claims, URL validation claims, IP address validation claims, date validation claims, credit card validation claims, domain validation claims, ISBN validation claims, ISSN validation claims, IBAN validation claims, UUID validation claims, semver validation claims, MAC address validation claims, scheduled execution claims, timeout claims, and cron-expression description claims. This family covers judging a cron-expression string only.

