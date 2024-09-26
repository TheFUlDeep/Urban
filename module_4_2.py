def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
# inner_function() # ошибка, потому что inner_function в локальном пространстве имен функции test_function
