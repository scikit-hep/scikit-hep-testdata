// https://github.com/scikit-hep/uproot5/pull/1043#issuecomment-1827565694

struct Foo { const std::string bar; };
Foo f;
TFile* outfile = TFile::Open("foobar.root", "recreate");
TTree* tree = new TTree("FooBar", "FooBar");
tree->Branch("Foo", &f);
tree->Fill();
outfile->Write();
outfile->Close();
