## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


class Version(object):
    """Version class according to `semantic versioning <https://semver.org>`_

    Comparison operators overloaded
    """
    def __init__(self, major, minor, patch):
        super(Version, self).__init__()
        assert(isinstance(major, int))
        assert(isinstance(minor, int))
        assert(isinstance(patch, int))
        self._major = major
        self._minor = minor
        self._patch = patch

    @staticmethod
    def fromString(string):
        """Constructs version class from string

        >>> v = Version.fromString("1.0.2")

        :param string: Version as string
        :type string: str
        """
        major, minor, patch = string.split('.')
        return Version(int(major), int(minor), int(patch))

    def __str__(self):
        return "{0}.{1}.{2}".format(self.major, self.minor, self.patch)

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor

    @property
    def patch(self):
        return self._patch

    def __eq__(self, other):
        return all([self.major == other.major,
                    self.minor == other.minor,
                    self.patch == other.patch])

    def __ge__(self, other):
        lhs = int("".join([str(self.major), str(self.minor), str(self.patch)]))
        rhs = int("".join([str(other.major), str(other.minor), str(other.patch)]))
        return lhs >= rhs

    def __gt__(self, other):
        lhs = int("".join([str(self.major), str(self.minor), str(self.patch)]))
        rhs = int("".join([str(other.major), str(other.minor), str(other.patch)]))
        return lhs > rhs


def currentVersion():
    """Returns current version of program
    """
    return Version(2, 0, 1)
