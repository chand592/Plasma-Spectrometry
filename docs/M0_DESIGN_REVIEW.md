# M0 design review — phone and home desk

Started: 25 September 2026. Status: **in progress**. Fill measured fields and attach your own photos before marking M0 complete.

## Decision record

| Decision | Current choice | Remaining check |
| --- | --- | --- |
| Measurement question | Repeatable visible emission-line positions from two sealed gases | No fusion claim. |
| Camera | Your phone | Record model, lens, image format and manual controls. |
| Workspace | Home desk | Measure clear surface and outlet; choose a dry location. |
| First source | Ordinary household visible lamp | Test optics before discharge source purchase; no Sun or laser. |
| Disperser | 1000 lines/mm transmission film | Record vendor, delivered cost and specification. |
| Housing | Opaque cardboard or foam board, then your CAD at MYFab | Test geometry before fabrication. |
| Later source | Intact Vernier ST-SPS and compatible tubes, borrowed if possible | Buy only after M1 and workspace review. |

## First optical sketch

```mermaid
flowchart LR
  A["Lamp or sealed tube"] --> B["Narrow slit"]
  B --> C["Opaque box and baffles"]
  C --> D["Transmission grating"]
  D --> E["Phone camera on fixed mount"]
```

The box, slit, grating and mount are your build. The source stays outside and has no electrical connection to the box. Rotate the grating and phone until a first-order spectrum falls in frame; shield the direct undispersed light. Make slit width and grating position adjustable in cardboard, then record actual dimensions after the first image. An incandescent lamp gives a broad continuum and an LED may show bands. Neither alone is a reliable multi-line wavelength standard.

**Desk envelope for the later source:** the ST-SPS body measures 26 × 18 × 29.5–38.0 cm, with the emitting region 21.5–30.0 cm above the bench. Reserve room for optical box, phone mount, cord routing and a stable gap. The manual specifies dry locations and warns that the tube gets hot. It does not publish a clearance distance. [Manufacturer manual](https://www.vernier.com/manuals/st-sps/).

## Measurements to take now

1. **Phone:** model, camera app, whether focus/exposure/white balance/HDR/file format can be controlled, dimensions and camera-bump position. Save a settings screenshot without personal data.
2. **Desk:** clear width × depth, outlet location, water/food/curtains/loose metal nearby, clamp position and lamp position. Take a dated wide photo of the cleared setup.
3. **Materials:** inventory dark cardboard/foam board, black tape, ruler, cutting mat and knife, clips, mount and ordinary lamp.
4. **Grating:** document supplier, 1000 lines/mm specification, mount size and delivered price. Candidate: [SCIEDCO Canada 50 mm mounted film](https://sciedco.ca/diffraction-interference/diffraction-grating-film-1000-lines-mm-in-50-mm-x-50-mm-cardboard-mount-22/), CA$2.70 listed 25 Sep 2026; quote shipping before ordering.

| Measurement | Your value |
| --- | --- |
| Phone model / main lens | TBD |
| Manual camera controls | TBD |
| Clear desk width × depth (cm) | TBD |
| Outlet relative to source (cm) | TBD |
| Housing maximum footprint (cm) | TBD after desk measurement |
| Grating delivered cost (CAD) | TBD |

## Hazard review and stopping rules

| Hazard | Boundary / check | Stop when |
| --- | --- | --- |
| Mains and internal 1.8 kV AC | Intact listed supply, adapter and carrier only; inspect, never open or wire. | Damage, moisture, odd smell/sound or unstable position. |
| Hot tube | Power off before changing; allow cooling; independent optical mount. | You need to touch an operating tube or the mount contacts it. |
| Cutting and optics | Cutting mat and suitable hand-tool practice; MYFab training for its equipment. | Unsafe cutting setup or damaged grating. |
| Light | Household lamps only for initial test; no Sun or laser. | Source too bright to capture without saturation. |
| Data | Save raw images and log geometry/settings. | Auto processing prevents comparison; document and redesign. |

The interlock encloses electrical parts, but the supply energizes a tube at **1.8 kV AC internally**. Turn it off before changing tubes. Read the whole [manual](https://www.vernier.com/manuals/st-sps/) before use; this is a design review, not operating instructions.

## MYFab route

For a rigid housing at U of T, complete MYFab two-tier online training and in-person orientation. Staff run 3D printing and laser cutting. Check its internal SharePoint with your U of T account for bookings, materials and charges; public contact: myhal.maker@utoronto.ca. [Facility information](https://www.engineering.utoronto.ca/myhal-centre-for-engineering-innovation-entrepreneurship/).

## M0 evidence and exit gate

Keep `evidence/M0/` locally; publish photos only if comfortable: dimensioned `design-sketch-v1`, `desk-photo`, `phone-settings`, `risk-review`, `bom-v1` with delivered prices, and `manual-notes` with reading date. Log each design change.

- [x] Choose phone and home desk.
- [x] Identify manual, dimensions, boundaries and grating candidate.
- [ ] Record phone model and camera controls.
- [ ] Measure desk and take photo.
- [ ] Inventory materials and quote grating delivery.
- [ ] Draw dimensioned sketch from measurements.
- [ ] Read manufacturer manual and sign/date risk review.

**M0 exit:** measurements filled, dimensioned sketch and workspace photo attached, first optical-only BOM reconciled to quote. Then start M1 with a household lamp.
