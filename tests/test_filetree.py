import nose
from git_serve.repo import GitServeRepo

def test_FileTree():
	test_input = [("foo/bar/baz",0),("foo/bar",0),("foo/zap",0)]
	r = GitServeRepo()
	assert r.index_to_tree(test_input) == { "foo" : { "bar" : { "baz" : {} }, "zap" : {} }}
