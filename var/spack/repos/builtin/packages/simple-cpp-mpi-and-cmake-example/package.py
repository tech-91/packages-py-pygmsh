# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class SimpleCppMpiAndCmakeExample(CMakePackage):
    """Paralelle Unstructured Grid Solver"""

    git = "https://gitlab.com/Te_ch/simple-cpp-mpi-and-cmake-example.git"

    maintainers("tech-91")

    license("LGPL-3.0-only")

    version("master", branch="main")  # For compatibility

    depends_on("cmake", type="build")
    depends_on("mpi", type=all)
