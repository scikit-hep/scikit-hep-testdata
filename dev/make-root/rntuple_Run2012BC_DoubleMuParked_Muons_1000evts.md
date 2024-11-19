First, download `Run2012BC_DoubleMuParked_Muons.root` from [here](https://opendata.cern.ch/record/12341). Then, run the following commands in ROOT.

```cpp
auto importer = ROOT::Experimental::RNTupleImporter::Create("./Run2012BC_DoubleMuParked_Muons.root", "Events", "./Run2012BC_DoubleMuParked_Muons_1000evts_rntuple_v1-0-0-0.root");
auto c = importer.get();
c->SetMaxEntries(1000);
c->Import()
```
