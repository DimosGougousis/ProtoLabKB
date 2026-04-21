---
type: knowledge-article
process: 3d-printing
source_url: https://www.protolabs.com/resources/guides-and-trend-reports/metal-3d-printing-materials-guide/
fetched_at: 2026-04-21
summary: Comprehensive guide to metal 3D printing materials for DMLS covering stainless steel (17-4 PH, 316L), aluminum (AlSi10Mg), Inconel 718, cobalt chrome, and titanium (Ti6Al4V) with detailed mechanical property comparisons, heat treatment options, and post-processing considerations.
---

# Metal 3D Printing Materials: What to Know

## A comparison of metal materials available for direct metal laser sintering (DMLS)

---

## How are Metal 3D Printing Materials Produced?

Metal additive manufacturing has a long, historical arc. Needless to say, the idea of using a laser to melt beds of metal powder was beyond our ancestors in the ancient world. Humans first used metal powders to make parts 5,000 years ago in Egypt. The process they used, which is still used today, is called powder metallurgy. It starts with pouring metal powder into a mold, packing it down to form the net shape and get the powder to stick together. With enough heat and/or pressure, particles want to reduce the amount of surface area they take up which causes them to meld together, resulting in sintering.

Now, let's explore how the powders are made today using gas atomization. In this process, a stream of liquid metal is directed into a high-pressure blast of gas which breaks the metal up into small droplets. Basically, you end up with a metal mist that solidifies quickly into round particles of powder.

The process is similar to how Dippin' Dots are made. To get the nice spheres of ice cream, the mix drips into a chamber full of liquid nitrogen to make the spheres. The biggest benefit of using gas atomization to create the raw material for additive manufacturing is that it offers the highest consistency of sphericity and particle size. That enhances flowability and creates a nice, level bed of powder to draw on with a laser.

Knowing how the powder is made is just the first step in the process. The actual printing method has changed over the years. In the earliest days of experimentation with 3D-printed metals, engineers used selective laser sintering (SLS) which worked with a similar principle to powder metallurgy. However, instead of needing to make a mold, operators used computers to control a laser to sinter the powder.

The downside to this process, as well as for powder metallurgy, is that it leaves micro-gaps, or pores, in the parts, making them less robust and less mechanically sound. These parts frequently require post-processing to reduce the size of those micro-gaps and enhance part performance.

---

## Demystifying the Metal 3D Printing Process

Today, manufacturers create metal 3D-printed parts using direct metal laser sintering (DMLS), although you'll also hear the phrase direct metal laser melting (DMLM). The metal 3D printer melts each layer—first the support structures to the base plate, then the part itself—with a laser aimed onto a bed of metallic powder. But in this case, the laser is completely melting the powder into a liquid, as opposed to sintering during which no melting occurs. Once a single layer of powder is micro-welded, the build platform shifts down and a re-coater blade moves across the platform to deposit the next layer of powder into the build chamber. The process is repeated layer-by-layer until the build is complete.

Once the print is completed, finished parts undergo the following:

* Parts are brushed manually to remove most of the loose powder.
* While still fixtured in the support system, parts are put through a heat-treat cycle to remove stresses.
* Parts are removed from the platform and their support structures are separated.
* Parts are then finished with any needed bead blasting and/or deburring.

Final metal 3D-printed parts are nearly 100% dense—that's a substantial improvement over the SLS metal parts of the 1990s.

Still, there are quality considerations when your parts are removed from the printer, and a few solutions to help improve the mechanical and aesthetic properties of the final product.

Often, parts come out of the printer feeling slightly rough. That's caused by the process itself. When a layer of powder is sintered to a part, you get a sort of gradient from totally melted near the part itself to an area where not everything in the new layer sinters.

Machining, polishing, or bead-blasting can take care of these issues, though. While DMLS achieves nearly 100% density, using hot isostatic pressing (HIP) further reduces any remaining porosity.

---

## Metal 3D Printing Materials Overview

Metal 3D printing can produce parts in a variety of alloys, including: aluminum, cobalt chrome, Inconel 718, titanium, and two types of stainless steel, 17-4 PH and 316L. Here's a quick comparison of each.

| Material | Resolution | Condition | Ultimate Tensile Strength (ksi) | Yield Stress (ksi) | Elongation (%) | Hardness |
| --- | --- | --- | --- | --- | --- | --- |
| Stainless Steel (17-4 PH) | 20-30 μm | Solution & Aged (H900) | 198-199 | 178-179 | 13 | 42 HRC |
| Stainless Steel (316L) | 20-30 μm | Stress Relieved | 82-85 | 55-56 | 75-78 | 88-90 HRB |
| Aluminum (AlSi10Mg) | 20-40 μm | Stress Relieved | 39-50 | 26-33 | 8-15 | 42-59 HRB |
| Cobalt Chrome (Co28Cr6Mo) | 20-30 μm | As Built | 176-182 | 112-119 | 14-17 | 38-39 HRC |
| Inconel 718 | 20-60 μm | Stress Relieved | 139-144 | 83-98 | 36-40 | 27-33 HRC |
| Inconel 718 | 30-60 μm | Solution & Aged per AMS 5663 | 201-208 | 174-175 | 18-19 | 45-46 HRC |
| Titanium (Ti6Al4V) | 20-30 μm | Stress Relieved | 144-153 | 124-138 | 15-18 | 33-35 HRC |

*20 μm = high resolution (HR)
*30, 40, and 60 μm = normal resolution (NR)

These figures are approximate and dependent on a number of factors, including but not limited to, machine and process parameters. The information provided is therefore not binding and not deemed to be certified. When performance is critical, also consider independent lab testing of additive materials or final parts.

### Material Selection Guide

| | Aluminum (AlSi10Mg) | Cobalt Chrome (Co28Cr6Mo) | Inconel 718 | Stainless Steel (17-4 PH) | Stainless Steel (316L) | Titanium (Ti6Al4V) |
| --- | --- | --- | --- | --- | --- | --- |
| **Corrosion Resistance** | | X | X | X | X | X |
| **Dimensional Stability** | X | X | X | X | X | X |
| **Durability** | | | | X | X | X |
| **Large Format** | X | | X | | | |
| **Lightweight** | X | | | | | X |
| **Strength** | | X | X | X | X | |
| **Strength-to-Weight** | X | | | | | X |
| **Stiffness** | X | X | X | X | | X |
| **Temperature Resistance** | | X | X | | | X |

---

## Surface Roughness and Finishing of Metal 3D-Printed Parts

The rapid heating and cooling of the metal material during the DMLS process results in a buildup of internal stresses. While every build undergoes a stress relief treatment per the ASTM 3301 standard, additional heat treatments can further improve mechanical properties like hardness, elongation, fatigue strength, and more.

### Hot Isostatic Pressing (HIP)

This process combines high pressure and temperature to eliminate any potential porosity within the part and reduce anisotropy. It also increases resistance to impact, wear, and abrasion, and improves fatigue characteristics. Typically, HIP is used for aerospace components that will be under heavy loads. HIP reduces much of the remaining internal micro-porosity by exposing the part to 2,000°F (1093°C) heat and very high pressure of 15,000psi (103.42 MPa) on all sides to fully solidify the part.

### Solution Annealing

The workpiece is heated above its recrystallization temperature and then cooled rapidly to relieve stresses and remove small imperfections in the microstructure. This is often used for stainless steel parts as it reduces hardness and increases ductility.

### Aging

This is a secondary heat treatment process applied to certain metal alloys. Part temperature is elevated and held for a designated time, causing precipitate formation. Our standard process is to age 17-4 stainless steel to the H900 condition. By request, Inconel 718 may be aged to boost temperature resistance, strength, and hardness properties.

While these heat-based processes address the mechanical properties of the part, another important concern with 3D printing is surface roughness. The most widely used measure of surface roughness is Ra, or the average roughness between a roughness profile and the mean line. Ra is the deviation from the ideal surface plane measured in microinches or micrometers. A larger Ra unit equates to a rougher surface.

Protolabs DMLS parts have a 200-400 microinch (5.08-10.16μm) Ra with standard finishing and 400-600 (10.16-15.24μm) as-printed. The difference in finish between our normal and high resolution is small. Polishing and machining are available to improve on the as-printed values noted above.

---

## Density, Weight, and Strength of Metal Printed Parts

There are two ways to think about density. The first is the mass of the material compared to the volume it occupies. Many times, material density is expressed in grams per cubic centimeter (g/cc).

The density of a metal will determine how much a part of a particular size weighs, and of course weight is an important consideration, especially in aerospace and automotive applications. Engineers and designers in those industries are always looking for ways to reduce component weight to meet emission standards, cut fuel consumption, consolidate many parts into fewer parts, and streamline overall product design.

Dense materials make strong parts—the higher the density, the greater the strength—which is why the percentage of density of a part's material is so crucial. Density is essentially the concentration of a given material in a given space.

Engineers and designers looking for lower-weight parts might turn to materials or alloys that are less dense. You should be cautious, though, because then you must consider the strength-to-weight ratio, too.

Topology optimization is a critical tool for removing weight while making sure that the part still has the required strength. It works by identifying which areas of the part see the highest loads, and which see little to no load and can therefore be removed. Often, this leads to organically shaped parts that would be hard to make with traditional methods like machining. Thankfully 3D printing makes these shapes possible.

The other way to think about density is in terms of porosity, or lack thereof. This is typically expressed as % density or % porosity. The DMLS process generally produces parts that are nearly 100% dense, although a small amount of porosity is typically present. We expect our DMLS parts to meet or exceed 99.5% density through our standard process. For applications that require the highest mechanical performance and fatigue resistance, the small amount of porosity present in a printed component can be reduced even further through hot isostatic pressing (HIP).

All metal additive parts, including those made using DMLS, can undergo radiographic testing to ensure porosity is minimal. X-ray scanning is a common choice for both metal additive parts and cast parts. The key benefit is that you can inspect the inside of the part for porosity without destroying it. Non-destructive radiographic inspection ensures that metal additive parts are free from the pores that could cause cracking while the part is in use.

---

## Comparing 3D-Printed and Machined Metals

Sometimes your designs give you the option to choose between 3D printing and CNC machining. Each has its own advantages, but we're here to focus on materials and how the manufacturing process affects them, if both can handle the geometries of your design:

### 3D printing offers:
* Potentially lesser mechanical properties compared to CNC machined parts, as they are typically not fully isotropic.
* Metals that would be difficult to machine (superalloys, in particular) can be 3D-printed.

### CNC machining characteristics:
* Excellent mechanical and thermal properties with fully isotropic behavior, meaning that the properties remain the same when tested in different directions.
* Dimensional restrictions from material blank or block sizes (using a non-standard blank size increases the manufacturing cost).
* A wide range of production-grade materials from which to choose.

Key material properties can also vary slightly between the two processes. A few comparisons of popular metals include:

Comparing materials that are available via both our 3D printing and CNC machining services (both stainless steels and titanium), you'll find that, in general, the printed parts have somewhat better elongation, hardness, and tensile strength.

The process you choose also affects the surface finish of your parts. Parts produced by both of these manufacturing processes can initially come out a bit rough. Those parts built by machining can come out, as some in the industry call it, "as-machined" or "as-milled." That means you're going to see some surface roughness and blemishes. Those parts produced by 3D printing will have more surface roughness or graininess, resembling the texture of a cast iron frying pan.

Fortunately, you can improve functionality and aesthetics of manufactured parts with a variety of post-process finishing options.

Several post-process options for machining can help protect parts and improve overall finish. Common processes include plating, anodizing, powder coating or painting, and more. Many of these processes can also be applied to metal additive parts.

For 3D printing, depending on the additive manufacturing technology, build direction, resolution, and materials chosen, you might see issues with part aesthetics. Here's a quick look at the 3D printing finishing options commonly offer and what you can expect as a result:

* **Standard**: Supported surfaces are sanded, and the entire part is finely blasted for a consistent look.
* **Custom Hand Polishing**: Parts undergo hand-sanding to achieve the desired finish. Finishes from a "machined surface" to near mirror finish are attainable. This is suitable for cosmetic surface finish improvements.
* **Post Machining**: In addition to a wealth of other machining operations, surfaces that need functional smoothness, such as sealing grooves, can be post machined.

Here's something you may want to consider: Post-processing machining on 3D-printed parts lets you get the complexity that machining alone can't achieve while ensuring critical features are to spec. It could be your ideal equation for metal manufacturing.

All in all, if you were to compare 3D metal-printed parts to any manufacturing process, casting would be the most appropriate. Both are based on a liquid turning into a solid and require designers to consider things like uniform wall thickness, avoiding sharp corners and more. The tensile strength of DMLS parts is generally as good or better than cast, but fatigue is worse. Using HIP, however, can address this issue.
