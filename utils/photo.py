import os
from typing import Optional, Self
from aiogram import types
from enum import Enum


class FileExtension(Enum):
    PNG = '.png'
    JPG = '.jpg'


class Photo:
    _BASE_DIR = "media/"

    def __new__(cls, *args, **kwargs) -> Self:
        cls._check_media_dir()
        return super().__new__(cls)

    def __del__(self):
        self._delete_photo()

    def __init__(self, message: types.Message, file_extension: Optional[str] = FileExtension.PNG.value) -> None:
        self._file_id = message.photo[-1].file_id
        self._file_name = self._file_id + file_extension
        self._file_path = self._BASE_DIR + self._file_name

    @classmethod
    def _check_media_dir(cls):
        if not os.path.exists(cls._BASE_DIR):
            os.makedirs(cls._BASE_DIR)

    def _delete_photo(self):
        if os.path.exists(self._file_path):
            os.remove(self._file_path)

    @property
    def file_id(self) -> str:
        return self._file_id

    @property
    def file_path(self) -> str:
        return self._file_path

    @property
    def file_name(self) -> str:
        return self._file_name
    
    @property
    def base_dir(self) -> str:
        return self._BASE_DIR
    
    # @base_dir.setter
    # def base_dir(self, base_dir: str):
    #     if type(base_dir) not in (str):
    #         raise TypeError(f"BASE_DIR must be str, not {type(base_dir)}")
    #     self._BASE_DIR = base_dir
