---
type: knowledge-article
process: 3d-printing
source_url: https://www.protolabs.com/resources/guides-and-trend-reports/mjf-vs-sls/
fetched_at: 2026-04-21
summary: Comparison of Multi Jet Fusion (MJF) and Selective Laser Sintering (SLS) 3D printing technologies. Note - The original URL returned a 404 error. This article contains general knowledge about both processes based on ProtoLabs guidelines.
---

# MJF vs SLS: Comparing Powder Bed 3D Printing Technologies

## Note on Source

The original URL for this article (https://www.protolabs.com/resources/guides-and-trend-reports/mjf-vs-sls/) returned a 404 error and was not accessible. The content below is compiled from general ProtoLabs knowledge about both technologies as referenced in other available documentation.

---

## Overview

Both Multi Jet Fusion (MJF) and Selective Laser Sintering (SLS) are powder bed fusion 3D printing technologies that use thermoplastic powders to create durable, functional parts. While they share similarities, there are key differences in how they work and the results they produce.

---

## How SLS Works

Selective Laser Sintering uses a high-powered laser to fuse tiny bits of nylon powder, tracing the geometry of digitally sliced CAD models layer by layer and working from the bottom of the part upwards. After each layer is complete, a roller spreads fresh material across the top of the bed and the process continues until the part is complete.

Key characteristics of SLS:
- Uses a laser to selectively sinter powder
- No support structures needed (excess powder supports the part)
- Good for complex geometries
- Parts may have slightly rougher surface finish
- More anisotropic properties (properties vary by direction)

---

## How MJF Works

Multi Jet Fusion, developed by HP, uses an inkjet array to deposit fusing and detailing agents across the print layer, and an infrared heating element fuses them. The process is similar to how a 2D inkjet printer works, but in three dimensions.

Key characteristics of MJF:
- Uses fusing and detailing agents with infrared heating
- No support structures needed
- Faster build times (entire layer fused at once)
- More isotropic properties (consistent in all directions)
- Better feature detail than SLS
- Currently more limited material selection

---

## Key Differences Summary

| Aspect | SLS | MJF |
| --- | --- | --- |
| **Fusing Method** | Laser scanning | Fusing agents + IR heating |
| **Build Speed** | Slower (laser traces each area) | Faster (entire layer at once) |
| **Surface Finish** | Slightly rougher | Smoother, better detail |
| **Isotropy** | More anisotropic | More isotropic |
| **Materials** | PA11, PA12, filled nylons, TPU | Primarily PA12 (expanding) |
| **Feature Detail** | Good | Better (smaller features possible) |
| **Cost** | Generally lower | Competitive, especially at scale |

---

## When to Choose SLS

- Need for proven, well-understood technology
- Require PA11 or specific filled nylon materials
- Cost is the primary driver
- Parts have less demanding feature detail requirements

## When to Choose MJF

- Need for more isotropic mechanical properties
- Better surface finish and feature detail required
- Faster lead times needed
- Building larger quantities of parts
- Working with living hinges or fine features

---

## Conclusion

Both SLS and MJF are excellent choices for producing durable, functional 3D-printed parts. The choice between them often comes down to specific application requirements, material needs, and production volume. As MJF technology continues to mature and expand its material offerings, the decision may become even more nuanced. Consulting with applications engineers can help determine the best technology for your specific project.
