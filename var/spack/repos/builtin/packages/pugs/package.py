# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Pugs(CMakePackage):
    """Paralelle Unstructured Grid Solver"""

    homepage = "https://gitlab.delpinux.fr/code/pugs"
    git = "https://gitlab.delpinux.fr/code/pugs.git"
    tags = []

    maintainers("tech-91")

    license("LGPL-3.0-only")

    # version("7.1.17", sha256="9c9c0fb507eb5c0d0f1f64a23909b3bda25652df737e935ea9336b08773afc4e")
    version("develop", branch="develop")
    version("master", branch="main", deprecated=True)  # For compatibility

    depends_on("cmake", type="build")
    # depends_on("hdf5", type=("build", "run"))
    # depends_on("gmsh", type=("build", "run"))
    # depends_on("metis", type=all)
    # depends_on("parmetis", type=all)
    # depends_on("mpi", type=all)
    # depends_on("petsc")
    # depends_on("slepc")
    # depends_on("kokkos +openmp +deprecated_code",type)
    # depends_on("ninja", type="build")

    # variant("shared_libs", values=bool, default=True,
    #         description="build shared libs")

    # variant("tests", values=bool, default=True,
    #         description="build testing")

    # variant("doc", values=bool, default=True,
    #         description="build testing")

    # variant("build_type", default="Release",
    #     description="The build type to build",
    #     values=("Debug", "Release", "Coverage"))

    # generator("ninja")
    # generator("make")
    # depends_on("py-flit-core@3.2:4", type="build", when="@1.3:")
    # depends_on("python@3.7:", type=("build", "run"))
    # depends_on("py-meshio@4.3.2:6", type=("build", "run"))
    # depends_on("py-gmsh", type=("build", "run"))
    # depends_on("py-numpy@1.20.0:1.26.4", type=("build", "run"))
    # def cmake_args(self):
    #     args = [
    #         # "-DPUGS_ENABLE_COSTO=ON"
    #         # "-DWHATEVER:STRING=somevalue",
    #         # self.define("ENABLE_BROKEN_FEATURE", False),
    #         self.define_from_variant("BUILD_SHARED_LIBS", "shared_libs"),
    #         self.define_from_variant("BUILD_TESTING", "tests"),
    #         self.define_from_variant("BUILD_DOXYGEN_DOC", "doc"),
    #         # self.define_from_variant("THREADS"), # True if +threads
    #     ]

    # return args
