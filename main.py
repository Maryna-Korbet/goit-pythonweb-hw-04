import argparse
import asyncio
import logging

from aiopath import AsyncPath
from aioshutil import copyfile


parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-S", help="Source folder", required=True)
parser.add_argument("--output", "-O", help="Output folder", default="dist")

args = vars(parser.parse_args())

source = AsyncPath(args.get("source"))
output = AsyncPath(args.get("output"))


async def read_folder(path: AsyncPath) -> None:
    """Recursively reading files in the source folder."""
    async for el in path.iterdir():
        if await el.is_dir():
            await read_folder(el)
        else:
            await copy_file(el)


async def copy_file(file: AsyncPath) -> None:
    """Copying the file to the appropriate subfolder by extension."""
    ext = file.suffix[1:] or "no_extension"
    ext_folder: AsyncPath = output / ext
    try:
        await ext_folder.mkdir(exist_ok=True, parents=True)
        await copyfile(file, ext_folder / file.name)
        logging.info(f"Copy: {file} -> {ext_folder / file.name}")
    except OSError as err:
        logging.error(f"Error copying {file}: {err}")


async def main():
    if not await source.exists() or not await source.is_dir():
        logging.error("Source folder does not exist or is not a directory.")
        return
    await read_folder(source)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    asyncio.run(main())