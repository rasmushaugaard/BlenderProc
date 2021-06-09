
from mathutils import Vector

from src.utility.sampler.Sphere import Sphere

class PartSphere:

    @staticmethod
    def sample(center: Vector, radius: float, mode: str, dist_above_center: float = 0.0, part_sphere_dir_vector: Vector = None) -> Vector:
        """ Samples a point from the surface or from the interior of solid sphere which is split in two parts.

        https://math.stackexchange.com/a/87238
        https://math.stackexchange.com/a/1585996

        :param center: Location of the center of the sphere.
        :param radius: The radius of the sphere.
        :param mode: Mode of sampling. Determines the geometrical structure used for sampling. Available: SURFACE (sampling
                     from the 2-sphere), INTERIOR (sampling from the 3-ball).
        :param dist_above_center: The distance above the center, which should be used. Default: 0.0 (half of the sphere).
        :param part_sphere_dir_vector: The direction in which the sphere should be split, the end point of the vector, will be in the middle of
                                       the sphere pointing towards the middle of the resulting surface. Default: [0, 0, 1].
        :return: A random point lying inside or on the surface of a solid sphere.
        """
        if part_sphere_dir_vector is None:
            part_sphere_dir_vector = Vector([0, 0, 1])
        part_sphere_dir_vector.normalize()

        if dist_above_center >= radius:
            raise Exception("The dist_above_center value is bigger or as big as the radius!")

        while True:
            location = Sphere.sample(center, radius, mode)
            # project the location onto the part_sphere_dir_vector and get the length
            loc_in_sphere = location - center
            length = loc_in_sphere.dot(part_sphere_dir_vector)
            if length > dist_above_center:
                return location
