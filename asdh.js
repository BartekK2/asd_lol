const fs = require("fs");
const path = require("path");

function loadCode(filename) {
    return fs.readFileSync(filename, "utf8");
}

const basePath = "C:\\Users\\barte\\Desktop\\asdh\\";  // Główna ścieżka

const responses = {
    quick_select: loadCode(basePath + "quick_select.py"),
    quick_sort: loadCode(basePath + "quick_sort.py"),
    heap_sort: loadCode(basePath + "kopce.py"),
    counting_sort: loadCode(basePath + "counting_sort.py"),
    mediana: loadCode(basePath + "mediana.py"),
    nnajw: loadCode(basePath + "nnajw.py"),
    radix_sort: loadCode(basePath + "radix_sort.py"),
    merge_sort: loadCode(basePath + "merge_sort.py"),
};

const args = process.argv.slice(2);

if (args.length === 0) {
    console.log("Podaj argument: 'quick_select, quick_sort, heap_sort, counting_sort, mediana, nnajw, radix_sort, merge_sort'");
    process.exit(1);
}

const arg = args[0].toLowerCase();

if (responses[arg]) {
    console.log(responses[arg]);
} else {
    console.log("Podaj argument: 'quick_select, quick_sort, heap_sort, counting_sort, mediana, nnajw, radix_sort, merge_sort'");

}
