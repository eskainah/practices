from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

#Now that you have set up your ManyToManyField to use your intermediary model 
# (Membership, in this case), you’re ready to start creating some many-to-many relationships. 
# You do this by creating instances of the intermediate model:
ringo = Person.objects.create(name="Ringo Starr")
paul = Person.objects.create(name="Paul McCartney")
beatles = Group.objects.create(name="The Beatles")
m1 = Membership(
...     person=ringo,
...     group=beatles,
...     date_joined=date(1962, 8, 16),
...     invite_reason="Needed a new drummer.",
... )
m1.save()
beatles.members.all()
#QuerySet [<Person: Ringo Starr>]>
ringo.group_set.all()
#QuerySet [<Group: The Beatles>]>
m2 = Membership.objects.create(
...     person=paul,
...     group=beatles,
...     date_joined=date(1960, 8, 1),
...     invite_reason="Wanted to form a band.",
... )
beatles.members.all()
#QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>]

#You can also use add(), create(), or set() to create relationships, as long as you specify through_defaults for any required fields:

beatles.members.add(john, through_defaults={"date_joined": date(1960, 8, 1)})
beatles.members.create(
...     name="George Harrison", through_defaults={"date_joined": date(1960, 8, 1)}
... )
beatles.members.set(
...     [john, paul, ringo, george], through_defaults={"date_joined": date(1960, 8, 1)}
... )
#You may prefer to create instances of the intermediate model directly.

#If the custom through table defined by the intermediate model does not enforce uniqueness on the (model1, model2) pair, allowing multiple values, the remove() call will remove all intermediate model instances:

Membership.objects.create(
...     person=ringo,
...     group=beatles,
...     date_joined=date(1968, 9, 4),
...     invite_reason="You've been gone for a month and we miss you.",
... )
beatles.members.all()
#<QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>, <Person: Ringo Starr>]>
# This deletes both of the intermediate model instances for Ringo Starr
beatles.members.remove(ringo)
beatles.members.all()
#<QuerySet [<Person: Paul McCartney>]>
#The clear() method can be used to remove all many-to-many relationships for an instance:

# Beatles have broken up
beatles.members.clear()
# Note that this deletes the intermediate model instances
Membership.objects.all()
#<QuerySet []>
#Once you have established the many-to-many relationships, you can issue queries. Just as with normal many-to-many relationships, you can query using the attributes of the many-to-many-related model:

# Find all the groups with a member whose name starts with 'Paul'
Group.objects.filter(members__name__startswith="Paul")
#<QuerySet [<Group: The Beatles>]>
#As you are using an intermediate model, you can also query on its attributes:

# Find all the members of the Beatles that joined after 1 Jan 1961
Person.objects.filter(
...     group__name="The Beatles", membership__date_joined__gt=date(1961, 1, 1)
... )
#<QuerySet [<Person: Ringo Starr]>
#If you need to access a membership’s information you may do so by directly querying the Membership model:

ringos_membership = Membership.objects.get(group=beatles, person=ringo)
ringos_membership.date_joined
datetime.date(1962, 8, 16)
ringos_membership.invite_reason
'Needed a new drummer.'
#Another way to access the same information is by querying the many-to-many reverse relationship from a Person object:

ringos_membership = ringo.membership_set.get(group=beatles)
ringos_membership.date_joined
datetime.date(1962, 8, 16)
ringos_membership.invite_reason
'Needed a new drummer.'
