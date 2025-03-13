# Copyright (c) 2025, Thiago de Melo <tmelo.mat@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from manim import *

OPAQUE = DARK_GRAY


class Path(VMobject):
    def __init__(self, points, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_points_as_corners(points)

    def get_important_points(self):
        return list(self.get_start_anchors()) + [self.get_end_anchors()[-1]]


class Koch(Scene):
    def construct(self):

        thiago = Text('T. de Melo and G. Biban',
                      font_size=12,
                      fill_opacity=.7,
                      color=WHITE
                      ).to_corner(DR, buff=0.2)
        self.add(thiago)

        new_scale = 1 / 3
        num_iteractions = 5
        line_stroke = DEFAULT_STROKE_WIDTH

        txt = Tex('$i=0$').to_corner(UP).set_color(BLUE).scale(1.3)
        points = [1.5 * LEFT, 1.5 * RIGHT]
        curve = Path(points).set_color(ORANGE).scale(3).shift(1 * DOWN)
        self.play(FadeIn(curve), FadeIn(txt))
        self.wait(.5)

        for i in range(1, num_iteractions + 1):
            self.remove(txt)
            txt = Tex(f'$i={i}$').to_corner(UP).set_color(BLUE).scale(1.3)

            left_curve = curve.copy()
            right_curve = curve.copy()

            ''' lado esquerdo '''
            A = left_curve.get_start()
            self.play(left_curve.animate
                      .set_color(OPAQUE)
                      #   .rotate(-PI / 4, about_point=A)
                      .scale(new_scale, about_point=A),
                      FadeIn(txt)
                      )

            left_stair = left_curve.copy()
            # B = left_stair.get_start()
            self.play(left_stair.animate
                      .set_color(OPAQUE)
                      .rotate(PI / 3, about_point=left_curve.get_start())
                      .move_to(left_curve.get_end(), aligned_edge=(LEFT+DOWN))
                      )

            ''' lado direito '''
            A = right_curve.get_end()
            self.play(right_curve.animate
                      .set_color(OPAQUE)
                      #   .rotate(-PI / 4, about_point=A)
                      .scale(new_scale, about_point=A),
                      #   FadeIn(txt)
                      )

            right_stair = right_curve.copy()
            # B = right_stair.get_start()
            self.play(right_stair.animate
                      .set_color(OPAQUE)
                      .rotate(- PI / 3, about_point=A)
                      .move_to(right_curve.get_start(), aligned_edge=(RIGHT+DOWN))
                      )

            self.remove(curve)

            if i > 3:
                line_stroke *= .8

            new_curve = Path(
                list(left_curve.get_important_points()) +
                list(left_stair.get_important_points()) +
                list(right_stair.get_important_points()) +
                list(right_curve.get_important_points()), stroke_width=line_stroke
            )

            self.play(Create(new_curve, run_time=1),
                      rate_func=linear,
                      )

            self.remove(left_curve, left_stair, right_curve, right_stair)
            curve = new_curve
            self.wait(.5)

        self.play(FadeOut(curve))
        self.wait(1)


class KochLPol(Scene):
    def construct(self):
        author = Text('T. de Melo and G. Biban',
                      font_size=12,
                      fill_opacity=.7,
                      color=WHITE
                      ).to_corner(DR, buff=0.2)
        self.add(author)

        new_scale = 1 / 3
        num_iteractions = 5
        line_stroke = DEFAULT_STROKE_WIDTH

        txt = Tex('$i=0$').to_corner(DOWN, buff=1).set_color(BLUE).scale(1.3)
        points = [1.5 * LEFT, 1.5 * RIGHT]
        curve = Path(points).set_color(WHITE).scale(3).shift(DOWN)
        self.play(FadeIn(curve), FadeIn(txt))
        self.wait(.5)

        for i in range(1, num_iteractions + 1):
            self.remove(txt)
            txt = Tex(f'$i={i}$').to_corner(
                DOWN, buff=1).set_color(BLUE).scale(1.3)

            left_curve = curve.copy()

            A = left_curve.get_start()
            self.play(left_curve.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=A),
                      FadeIn(txt)
                      )

            B = left_curve.get_end()
            left_stair = curve.copy()
            self.play(left_stair.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=B)
                      .rotate(PI / 2, about_point=left_curve.get_start())
                      .move_to(left_curve.get_end(), aligned_edge=(RIGHT+DOWN))
                      )

            C = left_stair.get_end()
            top = curve.copy()
            self.play(top.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=C)
                      .move_to(left_stair.get_end(), aligned_edge=(LEFT+DOWN))
                      )

            D = top.get_end()
            right_stair = curve.copy()
            self.play(right_stair.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=D)
                      .rotate(-PI/2, about_point=C)
                      .move_to(top.get_end(), aligned_edge=(LEFT+UP))
                      )

            E = right_stair.get_end()
            right_curve = curve.copy()
            self.play(right_curve.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=E)
                      .move_to(right_stair.get_end(), aligned_edge=(LEFT+DOWN))
                      )

            self.remove(curve)

            if i > 3:
                line_stroke *= .8

            new_curve = Path(
                list(left_curve.get_important_points()) +
                list(left_stair.get_important_points()) +
                list(top.get_important_points()) +
                list(right_stair.get_important_points()) +
                list(right_curve.get_important_points()), stroke_width=line_stroke
            )

            self.play(Create(new_curve, run_time=1),
                      rate_func=linear,
                      )

            self.remove(left_curve, left_stair, top, right_curve, right_stair)
            curve = new_curve
            self.wait(.5)

        self.play(FadeOut(curve))
        self.wait(1)


class KochAlt(Scene):
    def construct(self):
        author = Text('T. de Melo and G. Biban',
                      font_size=12,
                      fill_opacity=.7,
                      color=WHITE
                      ).to_corner(DR, buff=0.2)
        self.add(author)

        new_scale = 1 / 3
        num_iteractions = 5
        line_stroke = DEFAULT_STROKE_WIDTH

        txt = Tex('$i=0$').to_corner(UP).set_color(BLUE).scale(1.3)
        points = [1.5 * LEFT, 1.5 * RIGHT]
        curve = Path(points).set_color(ORANGE).scale(3).shift(DOWN)
        self.play(FadeIn(curve), FadeIn(txt))
        self.wait(.5)

        for i in range(1, num_iteractions + 1):
            self.remove(txt)
            txt = Tex(f'$i={i}$').to_corner(UP).set_color(BLUE).scale(1.3)

            left_curve = curve.copy()
            right_curve = curve.copy()

            ''' lado esquerdo '''
            A = left_curve.get_start()

            self.play(left_curve.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=A),
                      FadeIn(txt)
                      )

            if i == 2:
                self.play(left_curve.animate
                          .flip(LEFT)
                          .shift(np.sqrt(3)/2 * DOWN)
                          )
            if i > 2:
                self.play(left_curve.animate
                          .flip(LEFT)
                          .shift((np.sqrt(3)/3 * DOWN))
                          )

            left_stair = left_curve.copy()
            self.play(left_stair.animate
                      .set_color(OPAQUE)
                      .rotate(PI / 3, about_point=left_curve.get_start())
                      .move_to(left_curve.get_end(), aligned_edge=(LEFT+DOWN))
                      )

            ''' lado direito '''
            A = right_curve.get_end()

            self.play(right_curve.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=A)
                      )

            if i == 2:
                self.play(right_curve.animate
                          .flip(LEFT)
                          .shift(np.sqrt(3)/2 * DOWN)
                          )
            if i > 2:
                self.play(right_curve.animate
                          .flip(LEFT)
                          .shift((np.sqrt(3)/3 * DOWN))
                          )

            right_stair = right_curve.copy()
            self.play(right_stair.animate
                      .set_color(OPAQUE)
                      .rotate(- PI / 3, about_point=A)
                      .shift(3*LEFT)
                      )

            self.remove(curve)

            if i > 3:
                line_stroke *= .8

            new_curve = Path(
                list(left_curve.get_important_points())
                + list(left_stair.get_important_points())
                + list(right_stair.get_important_points())
                + list(right_curve.get_important_points()), stroke_width=line_stroke
            )

            self.play(Create(new_curve, run_time=1), rate_func=linear)

            self.remove(left_curve, left_stair, right_curve, right_stair)
            curve = new_curve
            self.wait(.5)

        self.play(FadeOut(curve))
        self.wait(1)


class KochSemiAlt(Scene):
    def construct(self):
        author = Text('T. de Melo and G. Biban',
                      font_size=12,
                      fill_opacity=.7,
                      color=WHITE
                      ).to_corner(DR, buff=0.2)
        self.add(author)

        new_scale = 1 / 3
        num_iteractions = 5
        line_stroke = DEFAULT_STROKE_WIDTH

        txt = Tex('$i=0$').to_corner(UP).set_color(BLUE).scale(1.3)
        points = [1.5 * LEFT, 1.5 * RIGHT]
        curve = Path(points).set_color(ORANGE).scale(3).shift(DOWN)
        self.play(FadeIn(curve), FadeIn(txt))
        self.wait(.5)

        for i in range(1, num_iteractions + 1):
            self.remove(txt)
            txt = Tex(f'$i={i}$').to_corner(UP).set_color(BLUE).scale(1.3)

            left_curve = curve.copy()
            right_curve = curve.copy()

            ''' lado esquerdo '''
            A = left_curve.get_start()
            self.play(left_curve.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=A),
                      FadeIn(txt)
                      )

            left_stair = left_curve.copy()
            B = left_stair.get_end()
            self.play(left_stair.animate
                      .set_color(OPAQUE)
                      .rotate(- 2 * PI / 3, about_point=B)
                      )

            ''' lado direito '''
            A = right_curve.get_end()
            self.play(right_curve.animate
                      .set_color(OPAQUE)
                      .scale(new_scale, about_point=A),
                      )

            right_stair = right_curve.copy()
            B = right_stair.get_start()
            self.play(right_stair.animate
                      .set_color(OPAQUE)
                      .rotate(2 * PI / 3, about_point=B)
                      )

            self.remove(curve)

            if i > 3:
                line_stroke *= .8

            new_curve = Path(
                list(left_curve.get_important_points()) +
                list(left_stair.get_important_points()[::-1]) +
                list(right_stair.get_important_points()[::-1]) +
                list(right_curve.get_important_points())
            )

            self.play(Create(new_curve, run_time=1), rate_func=linear)

            self.remove(left_curve, left_stair, right_curve, right_stair)
            curve = new_curve
            self.wait(.5)

        self.play(FadeOut(curve))
        self.wait(1)
