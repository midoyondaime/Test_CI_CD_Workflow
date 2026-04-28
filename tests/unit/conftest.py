import pytest


@pytest.fixture(scope="function")
def fixture_substract():
    data = [[1,4,-3],
            [-5,-1,-4],
            [0,7,-7],
            [1.5,1.3,0.2]]
    
    yield data


@pytest.fixture(scope="function")
def fixture_devide():
    data = [[2,4,0.5],
            [-5,-1,5],
            [0,7,-0],
            [1.5,2.1,0.7]]
    
    yield data