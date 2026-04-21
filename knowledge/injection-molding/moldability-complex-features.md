---
type: knowledge-article
process: injection-molding
source_url: https://www.protolabs.com/resources/guides-and-trend-reports/designing-for-moldability-complex-features/
fetched_at: 2026-04-21
summary: Advanced guide covering techniques for molding complex features including side-action cams, sliding shutoffs, and pickouts to achieve undercuts and through-holes without complex tooling.
---

# Designing for Moldability: Complex Features in Injection Molding

## See how the use of side-actions, sliding shutoffs, and pickouts can be used to injection mold undercuts and through-holes

Content in this Article

[Side-Action Cams](#side-actions "Side-Action Cams")
[Sliding Shutoffs](#shutoffs "Sliding Shutoffs")
[Pickouts](#pickouts "Pickouts")

Houses in Monopoly land have no doors or windows. Maybe the tiny people who live there spend a lot of time indoors, or perhaps they've perfected teleportation. More likely, it's because doorless windowless plastic houses are easy to make in simple two-part molds.

In the real world—including the world of plastic parts—life is more complicated. Houses have doors, and parts have indentations, through-holes, and other features that don't point straight up or down and could act as undercuts in a two-part mold. Designers using rapid injection molding can address these challenges in a variety of ways, including side-action cams, sliding shutoffs, pickouts, and bumpoffs.

![3D rendering of monopoly house with undercuts made with side-action cams](/media/6078/dfm2-figure1.jpg?width=285&height=154&v=1d2883296c486d0)

Figure 1: Side-action cams are a common solution to small undercuts in injection molding designs.

## Side-Action Cams

The most obvious approach to undercuts is side-actions—mold pieces that act from the outside of the part, moving perpendicular to the direction of mold opening. These produce side-facing features in a closed mold and then automatically withdraw, allowing the A-side mold half to withdraw, as the mold opens, and the part to be ejected from the B-side. In Figure 1, a side-action cam produces the door, sealing against the B-side core as the mold fills and then withdrawing to allow ejection. A similar technique could produce non-through indentations that would otherwise act as undercuts.

While side-actions are a relatively simple solution, there are a couple of things to keep in mind when using them. First, they must open perpendicular to the direction of mold opening. This would be simple if part walls didn't have to be drafted and were always positioned vertically. Since walls are not always conveniently oriented, however, care must be taken to ensure that side-actions operate (and are, themselves, drafted) perpendicular to the direction of mold opening and not necessarily perpendicular to the surfaces on which they live.

![improving moldability on complex features](/media/6079/dfm2-figure2.jpg?width=570&height=308&v=1d288329889b670)

Figure 2

Imagine the window in Figure 1 as a skylight in the roof rather than a dormer window. (See Figure 2). A window perpendicular to the angled roof would be partially trapped as the cam opens sideways. Fortunately, most CAD programs allow you to define the face or plane to which a feature should be oriented and drafted. In this case, in creating the skylight you would simply orient perpendicular to the plane of the parting line rather than that of the roof.

While cams are typically used to produce small features, they can also be used to produce large portions of a part. In Figure 3, we see a part's top and bottom that were formed by A- and B-side mold halves and its entire circumference is formed entirely by two cams.

![Molded part circumference formed by cams](/media/6080/dfm2-figure3.jpg?width=285&height=154&v=1d288329a092a80)

Feature 3: It is possible to form the entire circumference of a part with two cams by adjusting its orientation.

## Sliding Shutoffs

In some cases, you can eliminate the cost and complexity of side-actions by using simple two-part molds with strategically placed sliding shutoffs. This is an area in which faces of the A- and B-side mold halves move parallel to one another as the mold opens. If we remove the bottom sill from the door of the house, as shown in Figure 4, we can produce the features solely by the interaction of the A- and B-side mold halves.

When the mold is closed, a door-shaped pad extending from the B-side mold half seals against the wall of the A-side mold half. Because there is no sill under the door, the pad is not trapped and can exit through the bottom of the door as the mold opens.

![Using part orientation to achieve features](/media/6081/dfm2-figure4.jpg?width=285&height=154&v=1d288329bbd9140)

Figure 4: Clever use of the A- and B-side of a mold can eliminate the need for side-actions and reduce part cost.

Unlike a door formed by a side-action, which is drafted toward the outside of the house, a door formed by the B-side mold half is drafted toward the bottom of the house to facilitate part ejection. Similarly, the sliding shutoff itself—the area of the B-side mold half where the pad that forms the door meets the inside of the A-side mold half—must be drafted to a minimum of 3°. This is important for two reasons. The first is to allow a tight seal when the mold is clamped shut for injection. The second is to prevent wear of the mold surfaces as the mold opens. Shutoff wear can lead to leakage of resin between the mold faces resulting in flash which is unsightly and may interfere with part function.

![Hinge created with a sliding shutoff](/media/6082/dfm2-figure5.jpg?width=285&height=154&v=1d288329ceebe40)

Figure 5: Sliding shutoffs are one way to implement clips on molded parts.

Sliding shutoffs can be used to produce a variety of other useful features. One is a clip like the one in Figure 5. By its very nature, the hook at the end of a clip is specifically designed to catch, so the area under it would normally be an undercut. Creating a hole in the "floor" under the hook achieves the same end result as removing the sill under the door in the previous example. In this design, it allows a rectangular-shaped pad of one mold half to extend up through the floor to create the bottom of the hook and the recessed face of the clip. The rectangular-shaped pad shuts off against the walls of the other mold half, which produces the rest of the clip.

Another useful feature that can be formed using shutoffs is a through-hole that is perpendicular to the direction of mold opening. (See Figure 6.)

![Creating through-holes with sliding shutoffs](/media/6083/dfm2-figure6.jpg?width=285&height=154&v=1d288329e94f430)

Figure 6: Through-holes that are perpendicular to the mold opening are another common use of sliding shutoffs.

By removing alternating sections of the hole's wall, you can allow each mold half to form, alternately, inside and outside surfaces of the channel. The two mold halves meet at multiple points along the length of the through-hole and must be drafted at each of these points. This technique is demonstrated in our Design Cube, available for free at [get.protolabs.com/design-cube](https://get.protolabs.com/design-cube).

We've shown how removing a sill can eliminate the need for side-actions, but there are also instances in which a fully surrounded through-hole—a window for example—can be produced by sliding shutoffs. This is achieved by adding an increased amount of draft to a wall to allow the window to be formed partially by each of the two mold halves.

The window in Figure 7 is formed by the sliding shutoff shown in Figure 8. In this case, the shutoff between the two mold halves angles across the window.

![](/media/6084/dfm2-figure7.jpg?width=285&height=154&v=1d288329f856eb0)

Figure 7: Increasing draft can make it possible to create a fully surrounded through-hole.

The top edge of the window is formed by the B-side mold half; the bottom edge is formed by the A-side mold half. The two mold faces must be drafted by at least 3 degrees where they shut off (sliding shutoff). To allow this, the part wall itself must be drafted by more than 3 degrees. The additional amount by which the wall must be drafted depends on the part geometry.

How can you tell? Ask the following questions: (See Figure 8).

1. When looking down on your shutoff, can you clearly see edge 1 and edge 2? If 2 is hidden under 1, you cannot use this shutoff design.

2. Is the angle between edges 1 and 2 drafted at 3 degrees or greater?

![applying shutoffs to molded parts](/media/6085/dfm2-figure8.jpg?width=570&height=308&v=1d28832a122f210)

Figure 8

## Pickouts

In Protolabs' injection molding process, cams cannot form undercuts on non-exterior surfaces. In many cases, however, undercuts on interior surfaces can be formed using pickouts. These are inserts that are part of the mold when resin is injected, but are ejected with the part and then removed from the part, leaving undercut features in their place. By filling the undercut and becoming, temporarily, an element of the part, a pickout eliminates ejection problems.

## Key Topics Covered

- Side actions and cam actions
- Threaded features and unscrewing mechanisms
- Living hinges
- Overmolding considerations
- Insert molding techniques
- Complex surface textures
- Multi-shot molding
- Collapsible cores

## See Also

- [Injection Molding Knowledge Index](./_index.md)
- [Moldability: Fundamentals](./moldability-fundamentals.md)
- [Overmolding and Insert Molding](./overmolding-insert-molding.md)
