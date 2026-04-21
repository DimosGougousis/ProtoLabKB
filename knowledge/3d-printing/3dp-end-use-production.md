---
type: knowledge-article
process: 3d-printing
source_url: https://www.protolabs.com/resources/guides-and-trend-reports/3d-printing-for-end-use-production/
fetched_at: 2026-04-21
summary: Analysis of additive manufacturing technologies for end-use production parts, comparing plastic technologies (SLS, MJF, FDM, Carbon) and metal technologies (DMLS, Desktop Metal), with real-world case studies from GE Aviation, BMW, Johnson & Johnson, and others.
---

# 3D Printing for End-Use Production

## An analysis of additive technologies that are redefining 3D printing as an end-use manufacturing method

Over the past three decades, 3D printing has developed a reputation as an essential manufacturing process for prototype parts. Create a CAD model of your design, send it to your company's printer, and a 3D replica will be ready in hours. Yet these parts are often little more than conceptual show-and-tell models, not durable enough for long-term use, and in some cases prone to degradation by sunlight.

The winds of manufacturing are beginning to shift, however, and industrial-grade 3D printing, or additive manufacturing, is now encroaching on machining, injection molding, and other conventional manufacturing processes. This white paper explores the new and existing technology leaders in this area, and assesses the capabilities of production for each 3D printing process.

---

## The Case for 3D-Printed Production Parts

Defining what is meant by *production* is an important first step. In a typical manufacturing scenario, prototype parts are produced for form, fit, and some function testing, and then either CNC machined or injection molded until quantities grow high enough to merit investment in high-volume production tooling. Production 3D printing shortcuts that process. Depending on the part and its intended use, it is oftentimes possible to print parts that will perform every bit as well (and in some cases better) than conventionally produced parts, and do so cost-effectively enough that downstream investment is delayed or even unnecessary.

One notable example is GE Aviation's use of 3D-printed fuel nozzles in its LEAP engine, a move that saves aircraft owners roughly $3 million per plane annually. In the medical space, Johnson and Johnson is one of many suppliers using 3D printing for customized surgical tools and patient-specific implants, providing a better outcome for patient and surgeon alike. Oreck leveraged 3D printing to reduce the cost of its vacuum cleaner assembly pallets by 65 percent. Audio manufacturer Soundz used it to reduce tweeter grill lead-times from months to days. BMW used it to reduce the weight of handheld assembly tools by 72 percent. Without 3D printing, all of these parts would have required lengthy, expensive machining or injection molding operations to produce.

Granted, 3D printing cannot compete with high-volume production methods in the majority of applications, and probably won't for some time to come. However, it's important to note the willingness of these and literally thousands of other companies to embrace additive manufacturing technology for what it is—an effective way to produce precision components, which are often as capable as their machined or injection-molded counterparts when it comes to manufacturing end-use production parts.

---

## Comparing 3D Printing Technology

Much of this is made possible by a handful of 3D printing technologies, all of which can be grouped according to the types of materials they can use. Here's a short overview of each.

### Plastic Production

**Selective laser sintering (SLS)** is a powder bed printing technology. It uses a laser to fuse tiny bits of nylon powder, tracing the geometry of digitally sliced CAD models layer by layer and working from the bottom of the part upwards. After each layer is complete, a roller spreads fresh material across the top of the bed and the process continues until the part (or multi-part assembly) is complete. After a quick brushing to remove excess powder and a light bead blast, parts are ready for end-use; although a range of finishing processes are possible. Because nylon is a durable, multipurpose material, and because the entire volume of the heated powder bed can be used to build parts, SLS is a favorite of many designers for production of end-use mechanical components and commercial products in low-volume quantities.

**Multi Jet Fusion (MJF)** is a relatively new 3D printing technology launched by HP. It is similar to SLS in that it uses a powder bed and is currently limited to nylon polymers, although additional materials will almost certainly become available as the technology advances. There is no need for support material, post-processing is minimal, and the entire print chamber can be used to build parts. Instead of a laser, however, MJF employs an inkjet array to deposit fusing and detailing agents across the print layer, and an infrared heating element used to fuse them. The finished parts offer more consistent isotropic integrity than is possible with SLS, and because the entire bed is covered in each print pass (similar to a laser jet printer) build speed is predicated on the number of layers needed to build a part or batch of parts rather than on surface area.

**Fused deposition modeling (FDM)** uses a fishing reel-like filament of heated thermoplastic, depositing it in ultra-fine, side-by-side beads. Here again, parts are built one layer at a time, starting at the bottom. FDM prints its own scaffolding during the build process to support the workpiece, but these structures are easily dissolved in detergent and water once the part has been removed from the printer, after which the part is ready for use. A variety of commercial-grade materials such as ABS, nylon, polycarbonate, and PEI (Ultem) are available, and FDM can print multiple colors and even multiple parts within a single build.

**Carbon** is a newcomer to 3D printing and builds from the top down. It also builds parts "sans layers," using a proprietary technology known as CLIP (continuous liquid interface production), which projects a continuous sequence of part images into a UV-curable resin bath and literally "grows" the part in one fluid motion. When done, the parts are washed and then baked in an oven, triggering a chemical reaction that strengthens and cures the resin. Build speeds are substantially faster than competing processes (some say 100 times that of stereolithography). In addition, the UV light used to cure the resin is programmable, allowing users to tune material properties on the fly. For example, Carbon's polyurethane-like family of polymers can be made flexible like polypropylene, rigid like ABS, or elastomeric like thermoplastic olefin (TPO). The resulting parts can be used for production applications ranging from springs and gaskets to dental implants and manufacturing jigs.

### Metal Production

**Direct metal laser sintering (DMLS)** is another powder bed printing technology. It uses a laser to fuse aluminum, cobalt chrome, stainless steel, titanium, and other powdered alloys into fully dense metal parts, "drawing" them layer by layer from the bottom up. Because of the stresses built up during extreme temperatures involved (rapid heating and cooling), support structures are required during the build process to keep parts from curling or warping. When complete, parts must be heat-treated to remove residual stresses, after which the supports can be removed by machining or hand grinding. The GE fuel nozzles mentioned earlier are made using DMLS, as are an array of equally complex aerospace and end-use medical parts.

**Desktop Metal (DM)** is another newcomer to the 3D printing arena and offers two distinctly different, though complementary, metal printing technologies. Both boast of faster build rates than laser-based metal printers, as well as a wider array of alloys, and are geared toward higher production volumes. The two systems are:

* The *studio system* uses a process analogous to that of FDM, heating and then extruding rods made of powdered metal mixed with a polymer binder. When complete, the green parts are placed into a solvent for "debinding," removing a portion of the polymer and preparing the now "brown" parts for a subsequent trip to a 2,500-degree furnace. This fuses the individual metal particles one to another in a manner similar to metal injection molding (MIM). The result is a part nearly as dense as one that has been laser fused but without the accompanying thermal effects (or need for build supports), and suitable for most end-use applications.
* The *production system* uses a process known as single pass jetting (SPJ) and promises even faster build speeds. There's no need for debinding and brown parts can go straight into the sintering furnace. It also provides for full "nesting" of the build chamber, meaning many parts can be built in a single print job. And, as with the studio system, the support structures are easily removed—no secondary processing is required unless greater accuracy or finer finishes are required than that provided by the printer—an advantage in a production environment.

---

## Comparing 3D Printing Technologies

Here is a comparison chart to get started, although all specifications should be verified with the specific technology supplier or 3D printing partner before making any final decisions on your project:

| Technology | Available Materials | Max. Part Size | Min. Feature Size | Layer Thickness | Expected Tolerance |
| --- | --- | --- | --- | --- | --- |
| Direct Metal Laser Sintering | Many commonly used metals and super alloys | 9.68 in. x 9.68 in. x 10.8 in. (245.87mm x 245.87mm x 274.32mm) | 0.006 in. (0.152mm) in high-res. mode | 0.0008 in. (0.02mm) in high-res. mode | +/- 0.003 in. (0.076mm) |
| Desktop Metal Studio | 200+ metal alloys | 10 in. x 6.7 in. x 6.7 in. (255mm x 170mm x 170mm) post-shrink | N/A | 0.0012 in. (0.05mm) | N/A |
| Desktop Metal Production | 200+ metal alloys | 13 in. x 13 in. x 13 in. (330mm x 330mm x 330mm) build area | N/A | N/A | N/A |
| Selective Laser Sintering | Nylon-like PA850, PA650, filled nylon, and TPU | 19 in. x 19 in. x 22 in. (482mm x 482mm x 558mm) | 0.030 in. (0.76mm) | 0.004 in. (0.102mm) | +/- 0.003 in. (0.076mm) plus 0.001 in./in. |
| Fused Deposition Modeling | Similar to ABS, nylon, PC, PPSF, Ultem, and others | 36 in. x 24 in. x 36 in. (914.4mm x 609.6mm x 914.4 mm) | 0.019 in. (0.48mm) | 0.007 in. (0.178mm) to 0.020 in. (0.508mm), depending on material | +/- 0.0035 in. or +/-0.0015 in. per in. (+/- 0.089mm or +/- 0.0015mm per mm), whichever is greater |
| Multi Jet Fusion | Nylon-like PA650 (Nylon 12) | 11.1 in. x 14.9 in. x 14.9 in. (284mm x 380mm x 380mm) | 0.020 in. (0.5mm) | 0.003 in. (0.076mm) | +/- 0.004 in. (0.102mm) plus 0.001 in./in. |
| Carbon | Similar to ABS, polypropylene, TPO, glass-filled nylon, SLA resin | 7.4 in. x 4.6 in. x 12.8 in. (189mm x 118mm x 326mm) | Varies by material, but 0.004 in. (0.1mm) possible | N/A | Depends on material and part geometry, but assume 0.2% +/- 0.01 in. (0.3mm) of feature size |

---

## Conclusion

Your materials choice fundamentally affects the outcome of your parts, so it helps to have a general understanding of the advantages of each material available for your project. Here's a description of each:

**Aluminum (AlSi10Mg)** is comparable to the 3000 series alloy that is used in casting and die casting processes. It has good strength-to-weight ratio, high temperature and corrosion resistance, and good fatigue, creep and rupture strength. AlSi10Mg also exhibits thermal and electrical conductivity properties. Final parts built in AlSi10Mg receive stress relief application. Suitable industries: Aerospace and automotive, consumer goods, manufacturing, and construction.

**Cobalt Chrome (Co28Cr6Mo)** is a superalloy known for its high strength-to-weight ratio. It has high-performance tensile and creep characteristics and strong corrosion resistance. Suitable industries: Medical and dental, aerospace, industrial manufacturing, and jewelry.

**Inconel 718** is a high strength, corrosion resistant nickel-chromium superalloy ideal for parts that will experience extreme temperatures and mechanical loading. Final parts built in Inconel 718 receive a stress relief application. Solution and aging per AMS 5663 are also available to increase tensile strength and hardness. Suitable industries: Aerospace, energy, chemical processing, marine.

**Stainless Steel 17-4 PH** is a precipitation-hardened stainless steel that is known for its hardness and corrosion resistance. If you need to use stainless steel, select 17-4 PH for its significantly higher tensile strength and yield strength, but recognize that it has far less elongation at break than 316L. Final parts built using 17-4 PH receive vacuum solution heat treatment as well as H900 aging. Suitable industries: Aerospace, automotive, medical and dental, oil and gas, chemical processing, marine.

**Stainless Steel 316L** is a workhorse material used for manufacturing acid- and corrosion-resistant parts. Select 316L when stainless steel flexibility is needed as it is a more malleable material compared to 17-4 PH. Final parts built in 316L receive a stress relief application. Suitable industries: Medical and dental, food and beverage, chemical processing and pharmaceuticals, marine, oil and gas, jewelry, consumer goods.

**Titanium (Ti6Al4V)** is a workhorse alloy. Compared to Ti grade 23 annealed, the mechanical properties of Ti6Al4V are comparable to wrought titanium for tensile strength, elongation, and hardness. Final parts built in Ti6Al4V receive a vacuum stress relief application. Suitable industries: Aerospace and defense, medical and dental, automotive, consumer goods, bioprinting.
