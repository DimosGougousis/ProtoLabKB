---
type: knowledge-article
process: cnc-machining
source_url: https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/
fetched_at: 2026-04-21
summary: Comprehensive guide on designing complex features for CNC machined parts, covering hole placement, deep features, threads, text engraving, and corner radii with specific dimensional limits and best practices.
---

# CNC Machining Tips for Complex Parts

## Create highly complex machined parts faster and more efficiently with a few quick tips

CNC machine tools gain greater capabilities every year. Live-tool lathes can mill various shapes and drill off-axis or radial holes, operations that would once have required a separate trip to the milling department. And machining centers are equipped with indexing heads that support 3+2 machining, where multiple sides of the part can be completed in a single operation. This is good news for designer and engineer. Not only can extremely complex parts now be produced, but it can be done so with greater quality, lower cost, and shorter lead times.

But that doesn't mean anything goes—certain machining rules still apply—and not following them can lead to expensive reworks and project delays. This design tip explores some key considerations that any part designer should know including:

* Hole placement
* Milling deep features
* Threads and inserts
* Text
* Part radii

Protolabs has indexed or 3+2 milling. This feature allows the machine to grip the bottom of a workpiece and machine its top and sides in one handling. This milling enables the production of more complex parts—a bracket with undercuts along its sides, for example, or a Swiss cheese-like pneumatic manifold.

As with Protolabs' milling centers, CNC turning on high-speed lathes are able to complete many complex parts in a single operation. Live tooling and Y-axis capabilities mean it's possible to turn a bolt, mill the wrench flats, then drill a cross hole for a safety wire. More complex examples might include a hydraulic piston with alignment slots on one end, a fitting with spanner wrench holes on its face, or a shaft with an external keyway. In some cases, it's even possible to "turn" a part that's more orthogonal than it is round.

With this milling and live tooling background in mind, here are five elements to consider when designing complex parts:

**1. Hole Placement**

The minimum size for on-axis and axial holes on Protolabs' CNC lathes is 0.04 in. (1mm), with a maximum depth of 6x the diameter. Radial holes (those drilled from the side of the part) should be at least 0.08 in. (2mm) in diameter. Holes that go all the way through turned or milled parts are usually okay (especially on hollow or tube-shaped parts), but depending on the part size, hole diameter, and material, the cutting tool might not have enough reach. Protolabs will machine from each side when possible, but be sure to check your design analysis for potential constraints.

**2. Deep Features**

External grooves on a turned part cannot exceed 0.95 in. (24.1mm) in depth, or be narrower than 0.047 in. (1.2mm). All other slot-like milled features generally read from the same playbook as drilled holes in terms of size, but a good rule of thumb is to keep the depth less than 6x the feature width. Also, be sure to leave at least 0.020 in. (0.5mm) wall thickness on the adjacent material. Large flats and other milled surfaces—mill or lathe—depend entirely on the part geometry relative to the available cutter size. Deep ribs and grooves can be challenging though, wherever they're made. It is possible to cut heat sink-like features on a turned or milled part, but this depends on the actual part geometry and available tools. Again, check your DFM analysis carefully, and don't be afraid to test our software, or contact an applications engineer instead.

**3. Better Threads**

There's a great deal of overlap in threading capabilities between Protolabs' turning and milling centers. Generally speaking, Protolabs' automated factory can thread from #2-56 up to 1/2-20 (imperial) and M1.6x.35 up to M12x1.75 (metric) depending on the type of machine and the feature placement, although some exceptions exist. However, we can manufacture more types of threads via our semi-automated lane and even more options through our Protolabs Network. Check out the threading guidelines for precise measurements and details. While you're there, be sure to read the section about the proper way to model threads, and how this relates to internal vs. external and milled vs. turned part features. You might also think about using an insert. Coil and key inserts provide longer service life than bare threads, especially in soft materials like aluminum or plastic, and are easy for you to install, or they can be requested through our semi-automated factory or our Protolabs Network website.

**4. Texting Can Be Costly**

Complex aerospace and medical parts often require permanent marking of part numbers and company names. Recessed text may look nice, but it's also one of the more time-consuming of all machining operations and is downright prohibitive as production quantities rise. It's usually better to electrochemically etch or laser-mark parts, but if you must have engraved text, keep it short and sweet with simple, clean fonts. We recommend for soft metals and plastic Arial Rounded MT font 14 point 0.3mm deep, for hard metals Arial Rounded MT font 22 point 0.3mm deep. Our semi-automated factory or our Protolabs Network website offer Ink Pad printing and Laser Marking as well.

**5. Radii: Watch the Corners**

One common mistake on any machined part is the call out of sharp internal corners. For example, the turning tools typically used for finishing at Protolabs have a 0.016 in. (0.032mm) nose radius, so any mating parts should be designed with this in mind. Milling cutters go down to 0.040 in. (1mm), which means any pockets will contain internal corner radii a little more than half that. That's pretty sharp, but remember that milling with a tool that small takes a long time, and will be limited to a pocket no more than 0.375 in. (9.52mm) deep. The best bet is to relieve internal corners or allow for as large an internal radius as possible on mating part designs.

A final word of caution: Failing to apply good design for manufacturing practices makes challenging machining operations even more challenging, and therefore costly. Paying a bit more might be less of a concern on prototypes, but can be a real game changer when demand ramps up and parts move into production quantities. As always, when in doubt about any complex part or part feature, feel free to contact Protolabs with any questions at 877-479-3680 or [[email protected]](/cdn-cgi/l/email-protection).
