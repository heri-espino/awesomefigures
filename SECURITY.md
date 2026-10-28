# Security policy

## Supported versions

The `main` branch is the actively maintained development line. Once
versioned releases are published, support and fixes will be prioritized for
the latest supported release. Older releases are not guaranteed updates.
The project currently declares version `0.1.0` in its source metadata;
that alone does not imply a published release.

## Reporting a vulnerability

**Do not publish exploit details, private files, malicious TeX examples or
credentials in a public issue or pull request.**

1. Check the repository's **Security** tab for GitHub's private vulnerability
   reporting option. If available, use it to contact maintainers privately.
2. If private reporting is not enabled, request a confidential contact
   channel from an organization maintainer without including sensitive
   vulnerability details in the public request.
3. Include affected versions, platform, minimal reproduction steps, impact,
   and suggested mitigations through the private channel.

Please give maintainers a reasonable opportunity to investigate and address
the issue before public disclosure. No fixed response or remediation time
is promised.

## Scope and threat model

AwesomeFigures can invoke a local TeX engine using a manuscript's preamble.
**Only use trusted LaTeX sources**. TeX packages, class files, external assets,
and installed binaries are third-party code/resources. Figure rendering is
not a sandbox for adversarial manuscripts. Review input paths, temporary
files, dependency versions, and CI permissions when reporting issues.

Never commit credentials or customer/patient/private research data.
For general bug reports without security implications, use the regular
bug report template in GitHub Issues.
