import pytest
import os
from PQEnalyzer.read_files import read_energy_files, check_info_length

class TestReadFiles:
    """
    Test the read_energy_files function.
    """
    @pytest.mark.parametrize("example_dir", ["tests/data/"], indirect=False)
    def test__init__(self, example_dir):
        assert os.path.exists(example_dir + "md-01.en")
        assert os.path.exists(example_dir + "md-02.en")
        assert os.path.exists(example_dir + "md-03.en")
        assert os.path.exists(example_dir + "md-01.info")
        assert os.path.exists(example_dir + "md-02.info")
        assert os.path.exists(example_dir + "md-03.info")

        assert os.path.isfile(example_dir + "empty.en")
        assert os.path.isfile(example_dir + "empty.info")

    @pytest.mark.parametrize("example_dir", ["tests/data/"], indirect=False)
    def test_single_input(self, example_dir):
        list_filenames = [example_dir + "md-01.en"]

        energy_files = read_energy_files(list_filenames)

        assert len(energy_files) == 1

        energy = energy_files[0]
        assert len(energy.info) == 10

    @pytest.mark.parametrize("example_dir", ["tests/data/"], indirect=False)
    def test_multiple_inputs(self, example_dir):
        list_filenames = [example_dir + "md-02.en", example_dir + "md-03.en"]

        energy_files = read_energy_files(list_filenames)

        assert len(energy_files) == 2

        energy = energy_files[0]
        assert len(energy.info) == 12

        energy = energy_files[1]
        assert len(energy.info) == 12

    @pytest.mark.parametrize("example_dir", ["tests/data/"], indirect=False)
    def test_multiple_input_with_error(self, example_dir):
        list_filenames = [example_dir + "md-01.en", example_dir + "md-02.en"]

        with pytest.raises(ValueError):
            read_energy_files(list_filenames)

    def test_empty_input(self):
        list_filenames = []

        with pytest.raises(ValueError):
            read_energy_files(list_filenames)

    @pytest.mark.parametrize("example_dir", ["tests/data/"], indirect=False)
    def test_empty_file(self, example_dir):
        list_filenames = [example_dir + "empty.en"]

        with pytest.raises(ValueError):
            read_energy_files(list_filenames)