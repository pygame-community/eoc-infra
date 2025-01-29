from warelib.ware_callbacks import GeneratorWareCallback, WareCallback


eoc_globals_callbacks_schema: dict[str, type] = {
    "data": dict,
    "setup": WareCallback,
    "thumbnail": GeneratorWareCallback,
    "mainloop": GeneratorWareCallback,
}
