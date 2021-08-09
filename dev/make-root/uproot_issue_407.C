#include <TDatime.h>
#include <TFile.h>
#include <TObject.h>
#include <TTree.h>

class TFoo : public TObject {
public:
  TDatime d;
ClassDef(TFoo, 1);
};

class TFooPadded : public TObject {
public:
  TDatime d;
  // Pad the object to increase its size to fit version header that
  // TDatetime doesn't stream.  This is not needed for a test, but
  // shows a different error when custom streamer is not implemented.
  char pad[6];
ClassDef(TFooPadded, 1);
};

// Streaming interpreted classes is not supported, so this has to be ran with ACLiC:
//
//   root -lbq uproot_issue_407.C+
//
void uproot_issue_407() {
  TFile f("uproot-issue-407.root", "RECREATE");
  TTree tree;
  TDatime d;
  tree.Branch("branch", &d);
  d.Set(2021, 1, 1, 0, 0, 0);
  tree.Fill();
  tree.Fill();
  tree.Write("tree");
  TFoo foo;
  foo.d.Set(2021, 1, 1, 0, 0, 0);
  foo.Write("foo");
  TFooPadded foo_padded;
  foo_padded.d.Set(2021, 1, 1, 0, 0, 0);
  foo_padded.Write("foo_padded");
}
