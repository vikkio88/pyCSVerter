from vendors.voluptuous.voluptuous import Schema, Length, Range, All, Required

config = {
    'discard_not_ascii': True
}

rules = Schema({
    Required('name'): All(str, Length(min=3, max=200)),
    Required('address'): str,
    Required('stars'): All(int, Range(min=0, max=5)),
    Required('contact'): All(str, Length(min=3, max=300)),
    Required('phone'): All(str, Length(min=3, max=300)),
    # Required('uri'): All(str, Length(min=3, max=200))
})


def is_ascii(s):
    return all(ord(c) < 128 for c in s)
