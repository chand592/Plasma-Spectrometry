# Full project plan: home plasma spectroscopy station

## 1. Aim, limits, and success criteria

**Aim:** make a reliable optical instrument and use it to compare visible emission spectra from two sealed gas-discharge plasmas. The source is an intact, commercial, enclosed educational device. This project does not attempt nuclear fusion, expose high-voltage conductors, or put electrodes inside a homemade vacuum chamber.

**Primary deliverable:** identify several visible peaks in both gases, estimate their wavelengths and uncertainty, show repeatability across independent runs, and explain what the instrument cannot resolve. A beautiful image without measured uncertainty does not meet the goal.

**Suggested workload:** 6–10 weeks at 3–6 hours/week. This is a planning estimate; optical alignment and procurement can take longer.

### Milestone M0 — scope and purchasing gate (week 1)

1. Read the manufacturer's current supply/tube manual and `SAFETY.md`.
2. Choose a fixed camera with manual exposure/focus where possible; measure the available table space.
3. Decide whether MyFab can make your housing and complete its required access training if using it.
4. Prepare a one-page design sketch with source, slit, grating, camera, baffles, external support, and no electrical connection to the source.
5. Price and obtain only the optical prototype parts. Ask U of T teaching labs about borrowing a matched educational supply/tube set.

**Evidence:** dated design sketch, first BOM version with supplier links, copy/link to the read manual, workspace photo, and a brief risk assessment. **Exit:** source is selected and the optics can be developed without it.

### Milestone M1 — optical prototype (weeks 1–2)

1. Make an opaque box or printed housing that holds a slit, diffraction grating and camera. Start with simple cardboard; replace with your own CAD only after seeing a clear spectrum.
2. Use an ordinary visible lamp for initial alignment. Adjust until spectral bands remain in frame and the central undispersed light does not wash out the spectrum.
3. Lock focus, exposure, white balance and camera position for a capture session if your device permits. Do not use HDR or computational filters if they cannot be turned off.
4. Draw or model the second, more rigid housing. Add adjustment features that are mechanically useful, and record dimensions and revisions.

**Evidence:** CAD source and exported print file, bill of dimensions, 2–3 photos of the physical optical path, five raw alignment images, and a design log stating what changed. **Exit:** moving the instrument off and back onto a marked position produces qualitatively similar peak locations.

### Milestone M2 — quantitative calibration (weeks 3–4)

1. Capture a reference spectrum with multiple distinct visible lines, using the same physical camera geometry planned for the experiment.
2. Run `analysis/extract_profile.py` on an unedited image to export a pixel-versus-intensity CSV from a chosen strip. Record the strip coordinates. Choose unsaturated images.
3. Annotate the pixel coordinates of at least three distinct reference peaks and their accepted wavelengths, citing the reference table. Fit a first-pass wavelength calibration. A linear fit may be adequate over a narrow region; investigate residuals before choosing a more complex fit.
4. Keep one or more known lines out of the fit if feasible. Predict their wavelengths, calculate absolute errors and explain whether the result meets your chosen tolerance.
5. Measure how much the fit changes across independent captures and after repositioning the instrument. Never calibrate separately for each image and then claim repositioning repeatability.

**Suggested acceptance target:** a documented holdout error of **10 nm or less for a clearly resolved visible line**, or a candid explanation and redesign if the phone optics cannot achieve it. This is a project target, not a promised specification.

**Evidence:** calibration image, raw profile CSV, reference wavelengths and citations, fit equation/code, residual plot, holdout error table, and exact camera settings. **Exit:** calibration predicts at least one withheld feature within the stated uncertainty.

### Milestone M3 — two-gas measurement campaign (weeks 4–6)

1. Obtain the compatible commercial supply and two tubes only after the optical and safety gates. Hydrogen and argon/neon provide visually different spectra; hydrogen is a teaching gas sample, not fusion fuel in this experiment.
2. Make a run identifier before each capture; duplicate `experiments/RUN_LOG_TEMPLATE.md` as an individual log. Record tube identity, operator, room lighting, camera settings, geometry, source-on interval, and anomalies.
3. Capture **at least five independent images per gas**, removing/reseating the spectrometer between some runs. Save originals without edits; hash or list original filenames.
4. Capture at least one dark/control image with the source off and an ambient-light image. Avoid saturated peaks; choose the same camera settings for direct qualitative comparisons.
5. Extract profiles and annotate peak positions. Report identified and unidentified peaks separately; do not claim gas identification solely from one coincident line.

**Evidence:** 10+ raw images, controls, 10+ run logs, exported profiles, a table of peak positions and estimated wavelengths, a run-to-run spread figure. **Exit:** a reader can trace every figure to its original image and settings.

### Milestone M4 — report and demonstration (weeks 6–8)

Write a 4–8 page report or a thorough README linked to figures:

1. Question and why optical emission reveals gas-dependent transitions.
2. Hardware block diagram and measured dimensions; full parts list and actual receipts total.
3. Method, fixed and varied conditions, camera limitations and calibration method.
4. Results: raw example images, intensity profiles, calibration/residuals, peak table and uncertainty.
5. What went wrong: alignment drift, pixel saturation, mixed gas/ambient light, overlapping lines, sensitivity variations.
6. Conclusions bounded by evidence; no electron-temperature or fusion claim based only on the visible images.
7. Next iteration: mechanical improvement or better optical sensor, justified by the largest measured error.

Record a 1–2 minute demonstration of the intact source and external instrument. Avoid touching or opening the source while operating.

**Exit:** another student can regenerate the plots from published images and code; the report names limitations and distinguishes measured from inferred quantities.

### Milestone M5 — optional separate vacuum experiment (weeks 8–10)

Only if you want a stronger fluid-mechanics component: use a rated degassing chamber and its pump for **pressure-only** tests. Do not place the plasma source inside it, install electrodes, or connect it to electrical discharge hardware.

1. Inspect the chamber per the manufacturer; document its materials, pressure limits and gauge resolution.
2. Record pressure at regular intervals during pump-down. Compare with a simple exponential approximation, e.g. `P(t) ≈ P_end + (P_start − P_end) exp(−t/τ)` over a region where it fits, and state why real systems depart from it.
3. Isolate the chamber from the pump and record pressure rise versus time. Compare repeated tests and investigate gross leaks/venting behavior.
4. If comparing hose configurations, vary just one property and note that low-pressure gas transport can depart from elementary incompressible-fluid models.

**Evidence:** photo of rated kit/guarding, manufacturer instructions, raw time-pressure table, plots, fitted time constants, leak-rate estimate with gauge uncertainty, and a separate conclusion. The kit's supplied coarse gauge may only support qualitative analysis.

## 2. Skills and subject mapping

| Subject | What you practice | Evidence in portfolio |
| --- | --- | --- |
| Plasma/atomic physics | Ionization, excitation, emission lines; distinguish plasma from nuclear fusion. | Correct interpretation and cited line table. |
| Optics | Dispersion, spectral resolution, slit tradeoffs and stray light. | Optical CAD, resolution estimate and peak-width data. |
| Mechanical engineering | Dimensioned mounts, tolerances, iteration and assembly. | CAD revision history and repeatability test. |
| Instrumentation/metrology | Calibration, holdout test, controls, uncertainty and traceability. | Calibration residuals, run logs and raw images. |
| Coding/data analysis | Image processing, peak measurement and regenerable plots. | Python scripts and generated CSV/figures. |
| Controls | Camera acquisition settings and repeatable procedure; optional motorized optical positioning. **No direct plasma feedback control in the home build.** | Acquisition configuration and drift measurements. |
| Fluid mechanics/vacuum | Optional separate pump-down/leak study. **Not present in the sealed-tube core experiment.** | Time-pressure plots and limitations of model. |
| Thermal science | Tube warm-up/operating-time effects, within manufacturer instructions. | Timestamped intensity trends if measured. |
| Safety engineering | Hazard boundaries, equipment inspection and stop criteria. | Risk review and operating checklist. |

## 3. Evidence conventions

- Never overwrite or retouch `data/raw/`; produce any crops or contrast changes in `data/processed/` and label them.
- File naming example: `2026-10-12_run03_hydrogen_ambientoff.jpg`; attach a matching log.
- Record actual costs, revision dates and failed runs too. Put references and their access dates beside numerical line values.
- Distinguish camera counts from calibrated physical light intensity; a phone's channel values are not absolute spectral radiance.
- An uncertainty or a failed holdout is valuable evidence; do not hide it by fitting every line in the same dataset.

## 4. Future U of T extension

After M4, propose a **non-fusion, instrumented IEC demonstration chamber** to a faculty supervisor. Present the working optics and data, an experiment comparing grid geometry and plasma emission, and a facility/electrical/radiation review request. The lab chooses rated vacuum hardware, instrumentation, source, interlocks and applicable approvals. A vacuum resin kit is not reused as an IEC chamber. A D–D fusor would be a separate, higher-consequence project requiring neutron metrology and institutional oversight.
