# ex05: expected behavior

**Goal of the script:** for each review, a faithful summary, a correct sentiment label, and a
reply that addresses **that** customer's actual issue.

## What correct output looks like

| Review | Sentiment | Summary and reply must mention |
|---|---|---|
| R1 TrailLite backpack | negative | the shoulder strap snapping |
| R2 AquaPure bottle | positive | cold water / lid not leaking |
| R3 SnugFit gloves | negative | sizing and loose stitching |
| R4 BrightBeam headlamp | positive | battery life / beam |
| R5 CampEase stove | negative | ignition button / support not answering |
| R6 DryPack cover | positive | staying dry in rain |

- Support queue: **R1, R3, R5**.
- No prompt sent to the model contains an unfilled `{placeholder}`.
- Running the script twice gives the same labels.

## Sanity checks you can run

- Print each fully rendered prompt before it is sent.
- For each reply, can you tell which review it answers without looking at the id?
- Which steps need creativity, and which need to be deterministic?
