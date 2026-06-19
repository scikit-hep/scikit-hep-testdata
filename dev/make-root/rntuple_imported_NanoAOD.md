First, obtain a TTree-based NanoAOD file. Then, run the following commands in ROOT.

```cpp
auto importer = ROOT::Experimental::RNTupleImporter::Create("./cmsopendata2015_ttbar_19980_NANOAOD.root", "Events", "./cmsopendata2015_ttbar_19980_NANOAOD_RNTupleImporter_rntuple_v1-0-0-1.root");
auto c = importer.get();
c->SetMaxEntries(10);
c->Import()
```
