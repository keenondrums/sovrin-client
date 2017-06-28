import pytest

from sovrin_node.test.upgrade.conftest import validUpgrade
from sovrin_client.test.cli.constants import INVALID_SYNTAX
from plenum.common.util import randomString


def testPoolUpgradeHasInvalidSyntaxIfJustificationIsEmpty(be, do, validUpgrade, trusteeCli):
    validUpgrade['JUSTIFICATION'] = ''

    be(trusteeCli)
    do('send POOL_UPGRADE name={name} version={version} sha256={sha256} '
       'action={action} schedule={schedule} timeout={timeout}',
       mapper=validUpgrade, expect=INVALID_SYNTAX, within=10)


def testPoolUpgradeHasInvalidSyntaxIfJustificationIsVeryLong(be, do, validUpgrade, trusteeCli):
    validUpgrade['JUSTIFICATION'] = randomString(1001)

    be(trusteeCli)
    do('send POOL_UPGRADE name={name} version={version} sha256={sha256} '
       'action={action} schedule={schedule} timeout={timeout}',
       mapper=validUpgrade, expect=INVALID_SYNTAX, within=10)