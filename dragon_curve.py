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


class Dragon(Scene):
    def construct(self):

        author = Text('T. de Melo and G. Biban',
                      font_size=12,
                      fill_opacity=.7,
                      color=WHITE
                      ).to_corner(DR, buff=0.2)
        self.add(author)

        new_scale = 1 / np.sqrt(2)
        num_iteractions = 10

        txt = Tex('$i=0$').to_corner(UP).set_color(BLUE).scale(1.3)
        points = [2 * LEFT, 2 * RIGHT]
        curve = Path(points).set_color(ORANGE).scale(1.5).shift(0.5 * UP)
        self.play(FadeIn(curve), FadeIn(txt))
        self.wait(.5)

        for i in range(1, num_iteractions + 1):
            self.remove(txt)
            txt = Tex(f'$i={i}$').to_corner(UP).set_color(BLUE).scale(1.3)

            left_curve = curve.copy()
            A = left_curve.get_start()
            self.play(left_curve.animate
                      .set_color(OPAQUE)
                      .rotate(-PI / 4, about_point=A)
                      .scale(new_scale, about_point=A),
                      FadeIn(txt)
                      )

            right_curve = left_curve.copy()
            B = right_curve.get_end()
            self.play(right_curve.animate
                      .set_color(OPAQUE)
                      .rotate(-PI / 2, about_point=B)
                      )

            self.remove(curve)

            new_curve = Path(
                list(left_curve.get_important_points()) +
                list(right_curve.get_important_points()[::-1])
            ).set_color(ORANGE)

            self.play(Create(new_curve, run_time=1),
                      rate_func=linear,
                      )

            self.remove(left_curve, right_curve)
            curve = new_curve
            self.wait(.5)

        self.play(FadeOut(curve))
