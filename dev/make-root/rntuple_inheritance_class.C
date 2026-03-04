#include <ROOT/RNTupleModel.hxx>
#include <ROOT/RNTupleWriter.hxx>

#include <string>
#include <vector>

using ROOT::RNTupleModel;
using ROOT::RNTupleWriter;

struct BaseA {
  int              base_a1;
  double           base_a2;
  std::vector<int> base_a3;
};

struct BaseB {
  double base_b;
};

struct Child : public BaseA {
  int    child_1;
  double child_2;
};

struct GrandChild : public Child {
  int    grandchild_1;
  double grandchild_2;
};

struct MultiParent : public BaseA, BaseB {
  int    multi_parent_1;
  double multi_parent_2;
};

struct MultiGrandParent : public Child, MultiParent {
  int    multi_grand_parent1;
  double multi_grand_parent2;
};

void fill_BaseA( BaseA& obj, int i ) {
  obj.base_a1 = i;
  obj.base_a2 = i * 0.1;
  obj.base_a3.clear();
  for ( int j = 0; j < 3; j++ ) { obj.base_a3.push_back( i * j ); }
}

void fill_BaseB( BaseB& obj, int i ) { obj.base_b = i * 10.0; }

void fill_Child( Child& obj, int i ) {
  fill_BaseA( obj, i );
  obj.child_1 = i * 2;
  obj.child_2 = i * 20.0;
}

void fill_GrandChild( GrandChild& obj, int i ) {
  fill_Child( obj, i );
  obj.grandchild_1 = i * 3;
  obj.grandchild_2 = i * 30;
}

void fill_MultiParent( MultiParent& obj, int i ) {
  fill_BaseA( obj, i );
  fill_BaseB( obj, i );
  obj.multi_parent_1 = i * 4;
  obj.multi_parent_2 = i * 40.0;
}

void fill_MultiGrandParent( MultiGrandParent& obj, int i ) {
  fill_Child( obj, i );
  fill_MultiParent( obj, i );
  obj.multi_grand_parent1 = i * 5;
  obj.multi_grand_parent2 = i * 50.0;
}

void rntuple_inherited_structs() {
  std::string fname{ "test_class_inheritance_rntuple_v1-0-1-0.root" };

  auto model = RNTupleModel::Create();

  auto field_child             = model->MakeField<Child>( "child" );
  auto field_grandchild        = model->MakeField<GrandChild>( "grandchild" );
  auto field_multi_parent      = model->MakeField<MultiParent>( "multi_parent" );
  auto field_multi_grandparent = model->MakeField<MultiGrandParent>( "multi_grandparent" );

  auto writer = RNTupleWriter::Recreate( std::move( model ), "rntpl", fname );

  for ( int i = 0; i < 10; i++ )
  {
    fill_Child( *field_child, i );
    fill_GrandChild( *field_grandchild, i );
    fill_MultiParent( *field_multi_parent, i );
    fill_MultiGrandParent( *field_multi_grandparent, i );

    writer->Fill();
  }

  writer.reset();
}
