#pragma once

#ifdef _WIN32
#ifndef MYTEST_EXPORT_TEMPLATE
#define MYTEST_EXPORT_TEMPLATE
#endif
#ifndef MYTEST_EXPORT_PURE_INTERFACE
#define MYTEST_EXPORT_PURE_INTERFACE
#endif
#if (defined(MYTEST_EXPORTS) || defined(BUILDING_MYTEST))
#ifndef MYTEST_API
#define MYTEST_API __declspec(dllexport)
#endif
#else
#ifndef MYTEST_API
#define MYTEST_API __declspec(dllimport)
#endif
#endif
#else
#ifndef MYTEST_EXPORT_TEMPLATE
#define MYTEST_EXPORT_TEMPLATE __attribute__((visibility("default")))
#endif
#ifndef MYTEST_EXPORT_PURE_INTERFACE
#define MYTEST_EXPORT_PURE_INTERFACE __attribute__((visibility("default")))
#endif
#if (defined(MYTEST_EXPORTS) || defined(BUILDING_MYTEST))
#ifndef MYTEST_API
#define MYTEST_API __attribute__((visibility("default")))
#endif
#else
#ifndef MYTEST_API
#define MYTEST_API
#endif
#endif
#endif
