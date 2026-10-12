#include <TArrayF.h>
#include <TFile.h>
#include <TTree.h>

#include <vector>

// TArrayF member of a class stored in a split std::vector (scikit-hep/uproot5#1529).
// The entries cover several tracks, no tracks, and an empty TArrayF.

class MyTrack {
public:
  MyTrack() {}
  MyTrack(int n) {
    fPositions.Set(n);
    for (int i = 0; i < n; i++) fPositions[i] = i + 1;
  }

private:
  TArrayF fPositions;
};

class MyEvent {
public:
  void ClearTracks() { fTracks.clear(); }
  void AddTrack(MyTrack track) { fTracks.push_back(track); }

private:
  std::vector<MyTrack> fTracks;
};

// Run with:
//
//   root -l -b -q uproot_issue_1529.C
//
void uproot_issue_1529() {
  TFile f("uproot-issue-1529.root", "RECREATE");
  TTree tree("Test", "Test");
  MyEvent *ev = new MyEvent();
  tree.Branch("Event", &ev);

  ev->AddTrack(MyTrack(3));
  ev->AddTrack(MyTrack(1));
  tree.Fill();  // two tracks
  ev->ClearTracks();

  tree.Fill();  // no tracks

  ev->AddTrack(MyTrack(0));
  tree.Fill();  // empty TArrayF
  ev->ClearTracks();

  ev->AddTrack(MyTrack(2));
  tree.Fill();

  tree.Write();
  f.Close();
}
