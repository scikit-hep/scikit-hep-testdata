#include <TFile.h>
#include <TObject.h>
#include <TTree.h>

class TMyObject : public TObject {
  private:
    int value;

  public:
    TMyObject( int i ) : value( i ) {}

    ClassDef( TMyObject, 1 );
};

void uproot_issue_1502() {
    TFile f( "uproot-issue-1502.root", "RECREATE" );
    TTree tree( "tree", "tree" );

    TMyObject obj{ 0 };

    tree.Branch( "branch", &obj );

    for ( int i = 0; i < 10; i++ )
    {
        obj = TMyObject( i );
        tree.Fill();
    }

    tree.Write();
    f.Close();
}
