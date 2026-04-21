---
type: knowledge-article
process: 3d-printing
source_url: https://www.protolabs.com/resources/guides-and-trend-reports/selecting-the-right-material-for-3d-printing/
fetched_at: 2026-04-21
summary: Comprehensive guide to selecting 3D printing materials covering DMLS metals (stainless steel, aluminum, Inconel, cobalt chrome, titanium), SLA photopolymers (ABS-like, PC-like, PP-like, MicroFine), SLS/MJF thermoplastics (nylons, TPU, polypropylene), and PolyJet materials with detailed mechanical property comparisons.
---

# A Guide to 3D Printing Materials

## We 3D-printed sample parts from each of our materials and performed mechanical testing to accurately compare the properties between all of our material options.

Materials must be well-suited for the application in order to achieve design goals. The properties of any material become increasingly important as a product progresses from concept and functional prototyping to production.

However, material properties should only be evaluated in conjunction with the manufacturing process. It is the combination of the material and the process, inclusive of post-processing, that dictates the characteristics. For example, the same metal alloy shows different properties when die cast versus metal injection molded.

Additive manufacturing (AM), or 3D printing, is unique to other manufacturing processes, therefore the characteristics of produced parts are different, even when using a nearly identical alloy or plastic. AM benefits from recent investment and R&D efforts dedicated to the creation of materials specifically designed for industrial-grade 3D printers. In terms of mechanical and physical properties, material selection hinges on the prioritization of design and desired quality requirements.

The following information will aid in the characterization and selection of materials from six widely used industrial 3D printing processes: direct metal laser sintering (DMLS), stereolithography (SLA), selective laser sintering (SLS), Multi Jet Fusion (MJF), and PolyJet (PJ).

---

## Material Advancements in 3D Printing

AM material advancements have pushed 3D printing uses beyond form and fit models and prototypes to functional parts for testing and ultimately end-use production. The customizable nature of 3D printing is perfect for low-volume, end-use parts such as wearables or even high performance aerospace components.

And while the output of 3D printing is different from that of other manufacturing processes, it can offer a suitable alternative when seeking a direct replacement. However, experimentation may take time because of 3D printing's differences that extend beyond, but are related to, material properties. For example, additive materials are still advancing to include rich sets of performance data that characterize materials over a range of conditions. In most cases, 3D printing users are presented with a single data sheet that contains a limited set of values. Those values are also likely to present a best case scenario based on testing of virgin material (unrecycled powders), for example.

Another complication is that 3D printing produces anisotropic properties where the values differ for the X, Y, and Z axes. The degree of anisotropy varies with each additive technology—direct metal laser sintering is the closest to isotropic, for example—but it should always be a consideration.

Material suppliers rarely publish material specifications that document the change in properties from one axis to another, as the data behind these specifications can vary greatly by material, process, and even type of machine. By designing for the additive manufacturing (DfAM) process and adjusting the build orientation, anisotropism or inadequate material properties can be overcome. To do this, leverage the experiences from past projects or that of a qualified service organization to fill any gaps that arise because of limited material property data.

---

## 3D Printing Materials: Definitions and Test Methods

Let's take a minute to define some key terms you will see throughout this guide.

**Ultimate tensile strength (UTS)** refers to the maximum stress the material can withstand before breaking.

**Tensile modulus**, or elastic modulus, refers to the material stiffness. The higher the modulus, the stiffer the material.

**Elongation (%)** refers to the ductility of the material. Think about stretching a material into a wire. A higher elongation % indicates a material is more likely to be able to stretch or elongate into a thin wire shape.

**Hardness** is measured and reported in HRC or HRB on the Rockwell scale for metals within this guide. For polymers, like PJ, durometers are reported. The higher the number, the harder the material.

**Heat Deflection Temperature (HDT)**, sometimes called heat distortion temperature, is the temperature at which deformation occurs when a rigid material is placed under a specific load.

---

## Direct Metal Laser Sintering (DMLS) Materials

DMLS uses pure metal powder forms to produce parts with properties that are generally accepted to be comparable to wrought metals when comparing them in the heat-treated condition. Because there is rapid melting and solidification of powder particles in a small, constantly moving spot, DMLS may yield differences in grain size and grain boundaries that affect material performance. Research is ongoing to characterize additively manufactured grain structures and impacts to parts, which will be altered with changes to support structures, laser parameters, layer thickness, and heat treatments like stress relief or hot isostatic pressing (HIP). Ultimately, grain structures can be advantageously manipulated to offer heightened mechanical properties in a DMLS part.

Of the six additive manufacturing processes discussed in this guide, DMLS produces parts with material properties that approach an isotropic state, meaning similar properties independent from direction of measurement.

### Comparing Workhorse Materials: 17-4 PH vs. 316L

**Stainless steel** is a commonly used DMLS material, and it is available in two grades here at Protolabs: 17-4 PH and 316L. Select 17-4 PH (precipitation hardened) for its significantly higher tensile strength and yield strength, but recognize that it has less elongation at break than 316L, which means that 17-4 is less malleable than 316L. If you need a steel part with some flexibility, go with 316L. Both 17-4 PH and 316L are corrosion resistant options, but 316L is better at resisting acids. Note that 17-4 may be heat treated with a vacuum solution heat treatment and an H900 aging heat treatment to improve mechanical properties, while 316L is only offered in the stress-relieved state.

### Stainless Steel: Material Properties Compared

| Grade | Heat Treatment | Ultimate Tensile Strength | Elongation | Hardness |
| --- | --- | --- | --- | --- |
| **316L** | Annealed | 74.7 ksi | 60% | 80 HRB |
| **DMLS NR 316L** | Stress Relieved | 92 ksi | 58% | 94 HRB |
| **DMLS HR 316L** | Stress Relieved | 89 ksi | 55% | 94 HRB |
| **Wrought 17-4 PH** | H900 | 210 ksi | 7% | 45 HRC |
| **DMLS NR 17-4 PH** | Heat Treated | 198 ksi | 13% | 42 HRC |
| **DMLS HR 17-4 PH** | Heat Treated | 199 ksi | 10% | 42 HRC |

### Conductive Metal Options

**Aluminum AlSi10Mg** is comparable to a 360.0F aluminum alloy that is used for die cast processes. AlSi10Mg has good strength-to-weight ratio, high temperature and corrosion resistance, and good fatigue, creep, and rupture strength. AlSi10Mg also exhibits thermal and electrical conductivity properties. Compared to die-cast aluminum, the properties for tensile strength are comparable. However, elongation at break is slightly higher when compared to the average for aluminum.

**Metal plating** is another manufacturing modality to keep in mind. When prototyping parts that would normally be die cast or machined from aluminum, magnesium, or zinc, consider metal plating as an option. We offer a PC-like SLA resin that can be metal plated. The core material is a ceramic-like (Advanced High Temp) composite SLA material that exhibits strength, stiffness, and temperature resistance. After SLA parts are built, they are electroplated with a prescribed thickness of structural copper and nickel.

### Aluminum: Material Properties Compared

| Grade | Heat Treatment | Ultimate Tensile Strength | Hardness |
| --- | --- | --- | --- |
| **Die-Cast Aluminum (360.0-F)** | n/a | 43.5 ksi | 37 HRB |
| **DMLS NR AlSi10Mg** | Stress Relieved | 50 ksi | 59 HRB |
| **DMLS HR AlSi10Mg** | Stress Relieved | 48 ksi | 46 HRB |

### Superalloys

**Inconel 718** is a nickel chromium superalloy used in a vast range of temperature applications (-423 degrees F-1,300 degrees F) such as high-heat aircraft engine components and low-temperature cryogenic applications. Its high-temperature strength is derived from its ability to create a thick, stable, passivating oxide layer at high temperatures. Inconel 718 also has good tensile, fatigue, creep, and rupture strength properties.

When solution-treated and aged per AMS 5663, Inconel 718 exhibits higher tensile strength and increased hardness, coupled with a reduction in elongation %. Inconel 718 parts as large as 31.5 in. x 15.7 in. x 19.7 in. (800mm x 400mm x 500mm) in size can be manufactured here at Protolabs in 60 micron layers.

### Inconel 718: Material Properties Compared

| Grade | Heat Treatment | Ultimate Tensile Strength | Hardness | Elongation |
| --- | --- | --- | --- | --- |
| **Wrought Inconel 718** | n/a | 160 ksi | 36 HRC | 25% |
| **DMLS NR (60 Microns) Inconel 718** | Solution & Aged | 201 ksi | 45 HRC | 19% |
| **DMLS NR (60 Microns) Inconel 718** | Stress Relieved | 139 ksi | 27 HRC | 40% |
| **DMLS NR Inconel 718** | Solution & Aged | 208 ksi | 46 HRC | 18% |
| **DMLS NR Inconel 718** | Stress Relieved | 144 ksi | 30 HRC | 39% |
| **DMLS HR Inconel 718** | Stress Relieved | 143 ksi | 33 HRC | 36% |

### A Superalloy for Specialty Applications

**Cobalt chrome (Co28Cr6Mo)** is another DMLS superalloy that is used for specialty applications within the aerospace and medical industries because of its strength-to-weight ratio, creep, and corrosion resistance properties. DMLS Co28Cr6Mo, as defined by ASTM F75, hardness values are in line with wrought Co28Cr6Mo, but ultimate tensile strength and elongation are not as closely aligned.

Note that if these DMLS Co28Cr6Mo samples received heat treatment, this separation would not be as notable.

### Cobalt Chrome: Material Properties Compared

| Grade | Heat Treatment | Ultimate Tensile Strength | Hardness | Elongation |
| --- | --- | --- | --- | --- |
| **Wrought Co28Cr6Mo** | n/a | 242 ksi | 39 HRC | 27% |
| **DMLS NR Co28Cr6Mo** | As Built | 176 ksi | 38 HRC | 14% |
| **DMLS HR Co28Cr6Mo** | As Built | 182 ksi | 39 HRC | 17% |

### Strong as Steel, but Lightweight

**Titanium Ti6Al4V**, similar to DMLS cobalt chrome, is most commonly used for aerospace and medical applications due to its strength-to-weight ratio, temperature resistance, and acid/corrosion resistance.

Compared to wrought Ti6Al4V, the mechanical properties of vacuum stress relieved Ti6Al4V are similar to wrought titanium for tensile strength, elongation, and hardness.

### Titanium: Material Properties Compared

| Grade | Heat Treatment | Ultimate Tensile Strength | Hardness | Elongation |
| --- | --- | --- | --- | --- |
| **Wrought Ti6Al4V** | n/a | 149.5 ksi | 35.3 HRC | 12% |
| **DMLS NR Ti6Al4V** | Stress Relieved | 144 ksi | 33 HRC | 18% |
| **DMLS HR Ti6Al4V** | Stress Relieved | 153 ksi | 15 HRC | 15% |

---

## Stereolithography (SLA) Materials

SLA materials are classified as photopolymers, thermoset resins cured with ultraviolet (UV) light. SLA offers the broadest selection of 3D-printable plastics with a large range of mechanical properties. Note that the impact strengths are generally much lower than those of common injection-molded thermoplastics. The range of SLA materials also offers options for color and various levels of opacity. Combined with quality surface finish and high feature resolution, SLA can produce parts that are comparable to injection molding in terms of performance and appearance. However, keep in mind that exposure to moisture and UV light may alter the appearance, size, and mechanical properties of SLA-printed parts over time.

### ABS-like Materials

**ABS-like White (Accura Xtreme White 200) and ABS-like Gray (Accura Xtreme Gray)** are widely used general purpose SLA materials. In terms of flexibility and strength, these materials fall between molded polypropylene and molded ABS, which makes them a good choice for functional prototypes, such as a snap fit. Xtreme is a durable SLA material; it has a high impact strength and a high elongation at break (EB) with mid-range in strength and stiffness. If heat deflection is a critical design requirements, ABS-Like Gray offers the highest HDT of the ABS-like SLA resins. Of note, parts as large as 29 in. (736.6mm) x 25 in. (635mm) x 21 in. (533.4mm) can be built with ABS-Like White so consider it a primary option if you require an extensive build size envelope.

**ABS-like Black (RenShape SL7820)** is another general purpose material option when black is the desired color. Its deep black color and glossy up-facing (during build orientation) surfaces offer the appearance of a molded part, while layer lines may be visible in a side profile. RenShape 7820 also has low moisture absorption (0.25% per ASTM D570) so that parts are more dimensionally stable. Compared to other SLA materials, it has mid-range values for mechanical properties.

**ABS-like Translucent/Clear (WaterShed XC 11122)** offers a unique combination of low moisture absorption (0.35% per ASTM D570) and near-colorless transparency. Secondary operations are required to achieve functional part clarity. Parts will also retain a very light blue hue afterward. While good for general-purpose applications, WaterShed is the best choice for flow-visualization models, light pipes, and lenses.

**MicroFine™** is a custom-formulated material available in gray and green that is exclusive to Protolabs. This ABS-like material is 3D-printed in our customized machinery to achieve high resolution features as small as 0.0025 in. (0.0635mm) MicroFine is ideal for small parts, generally less than 1 cubic inch. In terms of mechanical properties, MicroFine falls in the mid-range of SLA materials for tensile strength and modulus and on the low end for impact strength and elongation.

### Polypropylene-like Materials

**PP-like Translucent White (Somos 9120)** is the best option of the SLA resins when polypropylene-like properties are needed. This material is the most flexible SLA option.

### Polycarbonate-like Materials

**PC-like Translucent/Clear (Accura 60)** is an alternative to the general purpose ABS-like materials and WaterShed XC 11122 when stiffness or clarity are desired. Like WaterShed, this material can be custom-finished to achieve functional transparency. Accura 60 has the highest tensile strength and elastic modulus outside of the Advanced High Temp material options that can be thermal-cured to increase mechanical properties.

**PC-like Advanced High Temp (Accura 5530)** creates strong, stiff parts with high-temperature resistance values that exceed that of injection-molded polycarbonate. A thermal post-cure option can increase HDT as high as 482 degrees F (measured at 66 psi). However, the thermal curing process does make Accura 5530 less durable, resulting in a 50% reduction to elongation. Accura 5530 also has the highest tensile modulus of all the unfilled SLA materials, and it is known for being resistant to automotive fluids.

**Ceramic-like Advanced HighTemp (PerFORM)** exhibits the highest tensile strength and tensile modulus making it the stiffest performance material of the SLA materials. When the thermal cure option is applied to parts made from PerFORM, it exhibits the highest HDT as high as 514 degrees F (measured at 66 psi) of the SLA materials and superior HDT when compared to similar injection-molded materials.

### SLA Material Comparison Charts

| Material | Tensile Strength | Elongation | Tensile Modulus | Heat Deflection |
| --- | --- | --- | --- | --- |
| **Molded Polypropylene** | 4.7 ksi | 100% | 250 ksi | 164°F |
| **Molded ABS** | 6.6 ksi | 30% | 290 ksi | 200°F |
| **Molded Polycarbonate** | 8.6 ksi | 75% | 320 ksi | 265°F |
| **Ceramic-Like Advanced High Temp (PerFORM)** | 10.9 ksi | 1% | 1,523 ksi | 514°F |
| **PC-Like Advanced High Temp (Accura 5530)** | 6.5 ksi | 1.5% | 566 ksi | 410°F |
| **PC-Like Translucent/Clear (Accura 60)** | 10.8 ksi | 7% | 508 ksi | 129°F |
| **ABS-Like White (Accura Xtreme White 200)** | 7.9 ksi | 9% | 579 ksi | 117°F |
| **ABS-Like Black (RenShape SL7820)** | 7 ksi | 5% | 435 ksi | 124°F |
| **ABS-Like Translucent/Clear (WaterShed XC 11122)** | 7.9 ksi | 6% | 421 ksi | 123°F |
| **MicroFine™ (Gray and Green)** | 8.7 ksi | 8% | 377 ksi | 138°F |
| **ABS-Like Gray (Accura Xtreme Gray)** | 5.8 ksi | 9% | 290 ksi | 144°F |
| **PP-Like Translucent White (Somos 9120)** | 5 ksi | 25% | 232 ksi | 142°F |

---

## Selective Laser Sintering (SLS) & Multi Jet Fusion (MJF) Materials

Selective laser sintering and Multi Jet Fusion offer the most economical AM material choices. The SLS/MJF technologies use thermoplastic powder forms, predominantly polyamide (PA), to make functional parts that have greater toughness and higher impact strengths compared to SLA parts. SLS/MJF materials also offer high HDTs ranging from 315 degrees F to 370 degrees F (measured at 66 psi). SLS/MJF parts are durable and able to withstand wear and abrasion for functional testing. They can produce parts with flexibility, such as living hinges or snap features.

The density of SLS/MJF materials is close to that of traditionally manufactured parts. One added benefit of this technology is that no support structures are required when sintering and fusing the parts. If large parts are needed, SLS parts as large as 19 in. (482.6mm) x 19 in. (482.6mm) x 17 in. (431.8mm) can be manufactured. SLS/MJF parts do lack in providing the surface finish and fine feature details available with SLA. However, when going head to head, MJF slightly outperforms SLS when it comes to manufacturing fine feature details.

Generally, PAs, when compared to the average values of their injection-molded counterparts, have similar HDT values but lower mechanical properties. SLS/MJF material properties have a known degree of anisotropism when measured in the x-y plane or the z plane. Values reported in this guide account for both measurements.

### General Purpose Nylons

**PA 11 Black (PA 850)** delivers ductility and flexibility without sacrificing tensile strength and temperature resistance. These characteristics make PA 850 a popular general-purpose material. Its EB is the highest of all AM nylons. Another factor that distinguishes PA 850 is its uniform, deep-black color. Black has high contrast, which makes features pop, and it hides dirt, grease, and grime. Black is also desirable for optical applications due to its low reflectivity.

**PA 12 White (PA 650)** is another go-to material for general-purpose applications. PA 650 is the strongest of the unfilled nylon materials. It is stiffer than PA 850 with a slightly higher elastic modulus and has comparable tensile properties when measured in the x-y and z directions. While its EB is less than half that of PA 850, it's still one of the top performers in terms of ductility among the SLS PA materials.

**PA 12 Black** is a high tensile strength nylon manufactured using MJF. Final parts are dyed black, and they exhibit quality surface finishes and slightly more isotropic mechanical properties when compared to SLS. When more detail is required, this material can achieve smaller minimum feature resolution—0.02 in. (0.508mm)—as compared to SLS materials—0.03 in (0.762mm). PA 12 Black is the best material option for designs that incorporate living hinges.

### Filled Materials

**PA12 Mineral-Filled (PA620-MF)** is a 25% mineral fiber-filled PA powder. The fiber content significantly increases stiffness and HDT. It is a good material option when stiffness and high temperature resistance are important requirements. Due to the sintering process, fiber origination effects (i.e. differing mechanical properties based on fiber alignment and orientation) that can occur in injection-molded parts are largely eliminated with printed parts that use sintering-filled materials.

**PA12 40% Glass-Filled (PA614-GS)** is another PA powder loaded with glass spheres that make it stiff and dimensionally stable. This material is an ideal candidate for parts that require long-term wear resistance properties. Due to the glass additive, it has decreased impact and tensile strengths compared to other nylons. At 315 degrees F, PA614-GS has the lowest HDT of the AM nylons.

**PA 12 40% Glass-Filled Black** is another option if you are looking to use a filled MJF material. The biggest advantage offered by this material is the heat deflection temperature of 248 degrees F (120 degrees C) when measured at 264 psi, ranking second best after PA 12 Mineral-Filled.

### Specialty Materials

**TPU 70-A** is a thermoplastic polyurethane that combines rubber-like elasticity and elongation with good abrasion and impact resistance properties. The rubber-like quality of this material makes it ideal for seals, gaskets, grips, hoses, or any other application where excellent resistance under dynamic loading is required. This specialty material is the second-most flexible AM material at Protolabs behind the softest (Shore 30A) PJ material offered.

**Polypropylene Natural** offers chemical resistance properties that are top among the SLS and MJF material offerings. This material is a true polypropylene, not a polypropylene-like material. This tough and durable, yet flexible, material offers resistance to most acids and is a low-weight material option.

---

## PolyJet (PJ) Materials

**Digital photopolymer** parts are achieved with the PolyJet (PJ) printing process. PJ materials are available in multiple Shore A hardnesses and colors: clear/translucent, white, and black. Parts can even be printed with two-tone coloring aesthetics and ranges of durometers.

Digital photopolymers can be leveraged in a variety of 3D printing applications that incorporate flexible features. PJ materials are routinely used to prototype overmolded and liquid silicone rubber (LSR) parts such as: gaskets, seals, covers, and straps.

While digital photopolymer does mimic some mechanical properties of LSR there are inherent differences that result in altered behavior. One fundamental difference of the materials is viscoelastic creep. Creep is a change in strain as a function of time while the stress remains constant. We tested injection-molded LSR samples against our PolyJet materials for viscoelastic creep at both 60A and 30A durometer. The PolyJet materials show a high initial value before quickly dropping below the specified hardness. LSR showed slight drift at the beginning of the test but quickly leveled out to a consistent value that was unaffected by time. It is worth understanding these material differences if you are leveraging digital photopolymer as an LSR prototype material.

### PolyJet Materials Charts

| Shore A Durometer | Tensile Strength | Tensile Tear Strength | Elongation |
| --- | --- | --- | --- |
| **30A** | 399 psi | 85 psi | 245% |
| **40A** | 508 psi | 100 psi | 200% |
| **50A** | 508 psi | 114 psi | 190% |
| **60A** | 580 psi | 121 psi | 160% |
| **70A** | 725 psi | 185 psi | 130% |
| **80A** | 1,088 psi | 341 psi | 80% |
| **95A** | 1,740 psi | 398 psi | 60% |

---

## Conclusion

Spanning metals, thermoplastics, and thermosets, AM or 3D printing provides many different materials that can simulate, if not replace, those that are processed through conventional means. While 1:1 material matches for conventionally manufactured materials and AM materials are not achievable given the processing differences, the wide range of AM material options, and advancing material options, is key. There is a strong likelihood that critical mechanical and physical properties will be satisfied by an existing AM material. With the support of an informed, qualified 3D printing resource that can fill in the data gaps, the door is opened for designers to leverage the unique advantages that 3D printing materials and technologies offer.
