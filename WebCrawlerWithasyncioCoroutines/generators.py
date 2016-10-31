import inspect

# frame=None
#
# def foo():
#     bar()
#
#
# def bar():
#     global frame
#     frame = inspect.currentframe()
#
# foo()
# print(frame.f_code.co_name)
# caller_frame=frame.f_back
# print(caller_frame.f_code.co_name)


def gen_fn():
    result=yield 1
    print('result of yield: {}'.format(result))
    result2 = yield 2
    print('result of 2nd yield: {}'.format(result2))

    return 'done'

gen = gen_fn()
print(gen.gi_code.co_name)
print(gen.gi_frame.f_lasti)

# def createGenerator():
#     for i in range(5):
#         yield i*i
#
# gen=createGenerator()
#
# for i in gen:
#     print(i)
# print("---")
# for i in gen:
#     print(i)
#
# generator_bit=1<<5
# b=bool(createGenerator.__code__.co_flags & generator_bit)
# print(b)
# print(type(createGenerator))

