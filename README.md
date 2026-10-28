# Mahmoud Farid — Developer Portfolio

Live portfolio: https://mahmoudfarid0208.github.io/Portfolio/

This repository contains a responsive portfolio presenting Mahmoud Farid's Android development work, backend and CRM integrations, and AI-powered application features.

## Downloadable CV

The site links to `Mahmoud_Farid_CV.pdf`. The PDF is generated from `scripts/build_cv_pdf.py` using ReportLab. The GitHub Actions workflow in `.github/workflows/build-cv-pdf.yml` rebuilds and commits the downloadable PDF when the source script or portfolio page changes.

To build it locally:

```bash
python -m pip install reportlab
python scripts/build_cv_pdf.py --output Mahmoud_Farid_CV.pdf
```

## Portfolio notes

- App screenshots use demo data.
- Project summaries focus on work described in the portfolio and CV.
- The portfolio avoids displaying a fixed app count so the description remains consistent as the ecosystem evolves.
