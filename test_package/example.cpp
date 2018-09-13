#include <iostream>
#include "Hypodermic/Hypodermic.h"


class Test {
	
};

int main() {
	Hypodermic::ContainerBuilder builder;

	builder.registerType<Test>();

	auto container = builder.build();
}
