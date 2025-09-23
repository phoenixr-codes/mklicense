from attrs import define, field
from enum import StrEnum, auto
from pathlib import Path


class Permission(StrEnum):
    COMMERCIAL_USE = "Commercial use"
    DISTRIBUTION = "Distribution"
    MODIFICATION = "Modification"
    PATENT_USE = "Patent use"
    PRIVATE_USE = "Private use"


class Condition(StrEnum):
    DISCLOSE_SOURCE = "Disclose source"
    LICENSE_AND_COPYRIGHT_NOTICE = "License and copyright notice"
    LICENSE_AND_COPYRIGHT_NOTICE_FOR_SOURCE = "License and copyright notice for source"
    COPYRIGHT_NOTICE_FOR_AD_MATERIAL = "Copyright notice for advertising material"
    NETWORK_USE_IS_DISTRIBUTION = "Network use is distribution"
    SAME_LICENSE = "Same license"
    SAME_LICENSE_FOR_LIBRARY = "Same license (library)"
    SAME_LICENSE_FOR_FILE = "Same license (file)"
    STATE_CHANGES = "State changes"


class Limitation(StrEnum):
    LIABILITY = "Liability"
    TRADEMARK_USE = "Trademark use"
    WARRANTY = "Warranty"


@define(kw_only=True, eq=False)
class License:
    long_name: str
    short_name: str
    spdx: str
    content: str
    permissions: set[Permission]
    conditions: set[Condition]
    limitations: set[Limitation]


def _embed(file_stem: str) -> str:
    return Path(__file__).parent.joinpath("licenses", file_stem).with_suffix(".txt").read_text()


LICENSES = [
    License(
        long_name="MIT License",
        short_name="MIT",
        spdx="MIT",
        content=_embed("MIT"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="GNU Affero General Public License v3.0",
        short_name="GNU AGPLv3",
        spdx="AGPL-3.0-only",
        content=_embed("AGPL3"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PATENT_USE,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.DISCLOSE_SOURCE,
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
            Condition.NETWORK_USE_IS_DISTRIBUTION,
            Condition.SAME_LICENSE,
            Condition.STATE_CHANGES,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="GNU General Public License v3.0",
        short_name="GNU GPLv3",
        spdx="GPL-3.0-only",
        content=_embed("GPL3"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PATENT_USE,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.DISCLOSE_SOURCE,
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
            Condition.NETWORK_USE_IS_DISTRIBUTION,
            Condition.SAME_LICENSE,
            Condition.STATE_CHANGES,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="GNU Lesser General Public License v3.0",
        short_name="GNU LGPLv3",
        spdx="LGPL-3.0-only",
        content=_embed("LGPL3"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PATENT_USE,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.DISCLOSE_SOURCE,
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
            Condition.NETWORK_USE_IS_DISTRIBUTION,
            Condition.SAME_LICENSE_FOR_LIBRARY,
            Condition.STATE_CHANGES,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="Mozilla Public License 2.0",
        short_name="Mozilla Public License 2.0",
        spdx="MPL-2.0",
        content=_embed("MPL2"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PATENT_USE,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.DISCLOSE_SOURCE,
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
            Condition.SAME_LICENSE_FOR_FILE,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.TRADEMARK_USE,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="Apache License 2.0",
        short_name="Apache License 2.0",
        spdx="Apache-2.0",
        content=_embed("Apache2"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PATENT_USE,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
            Condition.STATE_CHANGES,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.TRADEMARK_USE,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="Boost Software License 1.0",
        short_name="BSL",
        spdx="BSL-1.0",
        content=_embed("BSL"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.LICENSE_AND_COPYRIGHT_NOTICE_FOR_SOURCE,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        }
    ),
    License(
        long_name="The Zero-Clause BSD License",
        short_name="Zero-Clause BSD",
        spdx="0BSD",
        content=_embed("BSD0"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions=set(),
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="The 2-Clause BSD License",
        short_name="2-Clause BSD",
        spdx="BSD-2-Clause",
        content=_embed("BSD2"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="The 1-Clause BSD License",
        short_name="1-Clause BSD",
        spdx="BSD-1-Clause",
        content=_embed("BSD1"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="The 3-Clause BSD License",
        short_name="3-Clause BSD",
        spdx="BSD-3-Clause",
        content=_embed("BSD3"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="The 4-Clause BSD License",
        short_name="4-Clause BSD",
        spdx="BSD-4-Clause",
        content=_embed("BSD4"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions={
            Condition.LICENSE_AND_COPYRIGHT_NOTICE,
            Condition.COPYRIGHT_NOTICE_FOR_AD_MATERIAL,
        },
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
    License(
        long_name="The Unlicense",
        short_name="Unlicense",
        spdx="Unlicense",
        content=_embed("Unlicense"),
        permissions={
            Permission.COMMERCIAL_USE,
            Permission.DISTRIBUTION,
            Permission.MODIFICATION,
            Permission.PRIVATE_USE,
        },
        conditions=set(),
        limitations={
            Limitation.LIABILITY,
            Limitation.WARRANTY,
        },
    ),
]
