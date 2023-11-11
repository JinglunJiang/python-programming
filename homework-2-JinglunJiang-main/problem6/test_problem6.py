import problem6


def fresh_data():
    return [
        {"name": "scott", "age": 29},
        {"name": "lauren", "age": 28},
        {"name": "paul", "age": 50},
    ]


def test_process_record_all_keys():
    data = {"name": "scott", "age": 29, "salary": 100000}
    result = problem6.process_record(
        data,
        {
            "age": lambda x: x + 1,
            "name": lambda s: s.title(),
            "salary": lambda x: x * 2,
        },
    )
    assert result == {"name": "Scott", "age": 30, "salary": 200000}


def test_process_record_some_keys():
    data = {"name": "scott", "age": 29, "salary": 100000}
    result = problem6.process_record(data, {"age": lambda x: x + 1})
    assert result == {"name": "scott", "age": 30, "salary": 100000}
    assert result is not data


def test_process_record_no_keys():
    data = {"name": "scott", "age": 29, "salary": 100000}
    result = problem6.process_record(data, {})
    # they should be equal but distinct
    assert result == data
    assert result is not data


def test_no_changes():
    result = problem6.transform_data(fresh_data())
    assert result == fresh_data()


def test_age_plus_one():
    result = problem6.transform_data(fresh_data(), age=lambda age: age + 1)
    assert result == [
        {"name": "scott", "age": 30},
        {"name": "lauren", "age": 29},
        {"name": "paul", "age": 51},
    ]


def test_no_modifications():
    # this test ensures that the original data is not modified
    orig = fresh_data()
    result = problem6.transform_data(orig, age=lambda age: age + 1)
    assert orig == fresh_data()


def test_several_changes():
    result = problem6.transform_data(
        fresh_data(), age=lambda age: age + 1, name=lambda name: name.upper()
    )
    assert result == [
        {"name": "SCOTT", "age": 30},
        {"name": "LAUREN", "age": 29},
        {"name": "PAUL", "age": 51},
    ]
