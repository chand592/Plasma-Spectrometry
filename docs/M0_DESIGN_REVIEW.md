# M0 design review — phone and home desk

Started: 25 September 2026. Status: **in progress**. Fill measured fields and attach your own photos before marking M0 complete.

## Decision record

| Decision | Current choice | Remaining check |
| --- | --- | --- |
| Measurement question | Repeatable visible emission-line positions from two sealed gases | No fusion claim. |
| Measurement camera | iPhone 15 Pro main 1× rear camera; Rapoo 720p webcam for optional alignment preview | Verify Rapoo model label; record phone app, image format and capture settings. |
| Workspace | Home desk | Measure clear surface and outlet; choose a dry location. |
| First source | Ordinary household visible lamp | Test optics before discharge source purchase; no Sun or laser. |
| Disperser | 1000 lines/mm transmission film | Record vendor, delivered cost and specification. |
| Housing | Opaque cardboard or foam board, then your CAD at MYFab | Test geometry before fabrication. |
| Later source | Intact Vernier ST-SPS and compatible tubes, borrowed if possible | Buy only after M1 and workspace review. |

## First optical sketch

The optical path is: lamp or sealed tube → narrow slit → opaque box and baffles → transmission grating → phone camera on fixed mount.

The box, slit, grating and mount are your build. The source stays outside and has no electrical connection to the box. Rotate the grating and phone until a first-order spectrum falls in frame; shield the direct undispersed light. Make slit width and grating position adjustable in cardboard, then record actual dimensions after the first image. An incandescent lamp gives a broad continuum and an LED may show bands. Neither alone is a reliable multi-line wavelength standard.

**Desk envelope for the later source:** the ST-SPS body measures 26 × 18 × 29.5–38.0 cm, with the emitting region 21.5–30.0 cm above the bench. Reserve room for optical box, phone mount, cord routing and a stable gap. The manual specifies dry locations and warns that the tube gets hot. It does not publish a clearance distance. [Manufacturer manual](https://www.vernier.com/manuals/st-sps/).

## Measurements to take now

1. **Phone:** use rear main 1× lens in Photo mode on a rigid mount. Hold the screen to set AE/AF Lock and adjust exposure so bright bands do not saturate. Keep framing and settings fixed across a series. Record app, still format and automatic processing settings; save a settings screenshot without personal data. Capture five stationary lamp frames to compare line positions and clipping. The Rapoo webcam can provide live alignment preview; check its model label before assuming specifications.
2. **Desk:** clear width × depth, outlet location, water/food/curtains/loose metal nearby, clamp position and lamp position. Take a dated wide photo of the cleared setup.
3. **Materials:** inventory dark cardboard/foam board, black tape, ruler, cutting mat and knife, clips, mount and ordinary lamp.
4. **Grating:** document supplier, 1000 lines/mm specification, mount size and delivered price. Candidate: [SCIEDCO Canada 50 mm mounted film](https://sciedco.ca/diffraction-interference/diffraction-grating-film-1000-lines-mm-in-50-mm-x-50-mm-cardboard-mount-22/), CA$2.70 listed 25 Sep 2026; quote shipping before ordering.

| Measurement | Your value |
| --- | --- |
| Phone model / main lens | iPhone 15 Pro / rear main 1× |
| Camera controls | AE/AF Lock and exposure adjustment available; confirm actual app and image format |
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
| Data | Save original images and log geometry/settings. | Auto processing prevents comparison; document and redesign. |

The interlock encloses electrical parts, but the supply energizes a tube at **1.8 kV AC internally**. Turn it off before changing tubes. Read the whole [manual](https://www.vernier.com/manuals/st-sps/) before use; this is a design review, not operating instructions.
