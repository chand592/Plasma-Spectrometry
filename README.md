# Home plasma spectroscopy station

A build and measurement project for a sealed gas-discharge plasma source, a student-built optical spectrometer, and reproducible analysis. **This is a plasma project, not a fusion device.** There is no deuterium handling, homemade high-voltage supply, or electrical feedthrough into a vacuum vessel.

## Project question

How accurately and repeatably can a low-cost camera-and-grating spectrometer locate visible emission lines from different sealed gas tubes?

## Target result

- A rigid, light-blocking camera spectrometer with its own CAD and assembly notes.
- Raw, unedited images of hydrogen plus one comparison gas, with metadata and repeat runs.
- A calibration with at least three reference lines, plus an independent holdout check where practicable.
- A Python analysis that extracts line positions, wavelength uncertainty, and an honest limitation statement.
- A short report and a demonstration video of the intact commercial plasma source and optical instrument.

## Start here

1. Read [the full project plan](docs/PROJECT_PLAN.md), including the safety and purchasing gates.
2. Review [the bill of materials](docs/BOM.md); check prices and stock again before buying.
3. Build a camera spectrometer against ordinary visible light sources before purchasing the discharge source. [Digital-Spectroscope](https://github.com/joshbrew/Digital-Spectroscope) is one optional reference for printable mounts; do not present its files as your own.
4. After the optical prototype works, use only the matched commercial sealed tube and enclosed supply, following the manufacturer's manual.
5. Record each run in [the run log template](experiments/RUN_LOG_TEMPLATE.md). Copy raw images into `data/raw/` only when you intend to publish them.
6. Use [the analysis script](analysis/extract_profile.py) to export a camera intensity profile; calibrate wavelength with your documented reference points and report errors.

## Milestones

| Milestone | Exit evidence |
| --- | --- |
| M0: scope and safety | Written scope, risk review, purchasing choices, and a planned capture station. |
| M1: optical prototype | CAD/photo, first dispersed image, repeatable alignment. |
| M2: calibrated instrument | Raw images, line annotations, fit and independent check. |
| M3: two-gas experiment | At least five independent captures per gas with fixed camera settings; run logs. |
| M4: analysis and report | Reproducible plots, error table, limitations, report and short demo. |
| M5: optional vacuum module | Separate rated chamber, pump-down traces and leak-rate fit; no electrical discharge in this module. |

## Repository layout

- `docs/PROJECT_PLAN.md` — complete schedule, methods, evidence checklist and study map.
- `docs/BOM.md` — procurement list and price provenance.
- `docs/SAFETY.md` — boundaries and operating checklist.
- `hardware/` — your original CAD files, dimensions, assembly photos and version notes.
- `analysis/` — profile extraction and your later calibration notebooks/scripts.
- `experiments/` — blank run log to duplicate for each session.
- `data/raw/` — source images, unedited; keep large files out of Git until ready to publish.
- `data/processed/` — exported profiles and plots regenerated from source images.

## References

- [Vernier Canada supply](https://www.verniercanada.ca/product/lab-equipment/spectrum-tube-single-power-supply/) and [matched sealed tubes](https://www.verniercanada.ca/product/accessories/spectrum-tubes/).
- [Vernier operating manual](https://www.vernier.com/manuals/st-sps/).
- [U of T MyFab](https://www.engineering.utoronto.ca/myhal-centre-for-engineering-innovation-entrepreneurship/).
- [Open-source printable spectrometer reference](https://github.com/joshbrew/Digital-Spectroscope).

This repository is a project plan and starter analysis, not a certification of any electrical or vacuum apparatus.
