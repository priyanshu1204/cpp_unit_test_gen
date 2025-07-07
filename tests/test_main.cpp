#include "gtest/gtest.h"
#include <iostream>

// Test case for the add function
TEST(AddTest, PositiveNumbers) {
  EXPECT_EQ(add(2, 3), 5);
}

TEST(AddTest, ZeroAndPositive) {
  EXPECT_EQ(add(0, 5), 5);
}

TEST(AddTest, NegativeAndPositive) {
  EXPECT_EQ(add(-2, 3), 1);
}

TEST(AddTest, TwoNegativeNumbers) {
  EXPECT_EQ(add(-2, -3), -5);
}

TEST(AddTest, ZeroAndZero) {
  EXPECT_EQ(add(0, 0), 0);
}