#include <mytest/mytest.hpp>

#include <gtest/gtest.h>

TEST(mytest, atest)
{
    ASSERT_NO_THROW(mytest::doMyTest());
}

TEST(mytest, btest)
{
    ASSERT_NO_THROW(mytest::doMyTest());
}

