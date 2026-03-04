#pragma once

#include <vector>

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
