from conans import ConanFile

class FreeFrameConan(ConanFile):
    name = 'freeframe'

    source_version = '1.6'
    package_version = '1'
    version = '%s-%s' % (source_version, package_version)

    settings = []
    url = 'http://freeframe.org/'
    license = 'https://sourceforge.net/p/freeframe/svn/HEAD/tree/branches/freeframe-1.6/FFGL-SDK/License.txt'
    description = 'Open-source cross-platform real-time video effects plugin system'
    source_dir = 'freeframe-%s' % source_version

    def source(self):
        self.run('svn checkout -N https://svn.code.sf.net/p/freeframe/svn/branches/freeframe-1.6/FFGL-SDK %s' % self.source_dir)
        self.run('svn update %s/Include' % self.source_dir)

        self.run('mv %s/License.txt %s/%s.txt' % (self.source_dir, self.source_dir, self.name))

    def package(self):
        self.copy('FreeFrame.h', src='%s/Include' % self.source_dir, dst='include')
        self.copy('FFGL.h', src='%s/Include' % self.source_dir, dst='include')

        self.copy('%s.txt' % self.name, src=self.source_dir, dst='license')
