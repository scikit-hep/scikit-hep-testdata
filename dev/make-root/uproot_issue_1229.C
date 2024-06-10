#include <TFile.h>
#include <TObject.h>
#include <TTree.h>

class TFooMember : public TObject {
public:
  TFooMember(int _value)
    : value(_value)
  {};

  int value;

ClassDef(TFooMember, 1);
};

class TFoo : public TObject {
public:
  TFoo(int value_for_member, int value_for_const_member)
    : pointer{new TFooMember(value_for_member)}
    , const_pointer{new TFooMember(value_for_const_member)}
  {};

  TFooMember *pointer;
  const TFooMember *const_pointer;

ClassDef(TFoo, 1);
};

// Streaming interpreted classes is not supported, so this has to be ran with ACLiC:
//
//   root -lbq uproot_issue_1229.C+
//
void uproot_issue_1229() {
  TFile f("uproot-issue-1229.root", "RECREATE");
  TTree tree;
  TFoo foo(123, 321);
  tree.Branch("branch", &foo);
  tree.Fill();
  tree.Write("tree");
}
