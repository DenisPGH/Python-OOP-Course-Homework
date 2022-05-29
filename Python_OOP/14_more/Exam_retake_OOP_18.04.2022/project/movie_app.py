from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection=[]
        self.users_collection=[]

    def register_user(self,username: str, age: int):
        for each_user in self.users_collection:
            if username ==each_user.username:
                raise Exception("User already exists!")
        self.users_collection.append(User(username,age))
        return f"{username} registered successfully."


    def upload_movie(self,username: str, movie: Movie):
        searched_user=''
        # user is owner
        if username !=movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for each_user in self.users_collection:
            if username==each_user.username:
                searched_user=each_user
        if searched_user=="":
            raise Exception("This user does not exist!")
        for each_movie in searched_user.movies_owned:
            if each_movie.title==movie.title:
                raise  Exception("Movie already added to the collection!")

        if searched_user.age>=movie.age_restriction:
            searched_user.movies_owned.append(movie)
            self.movies_collection.append(movie)
            return f"{username} successfully added {movie.title} movie."

    def edit_movie(self,username: str, movie: Movie, **kwargs):
        user=''
        name_owner_of_movie=movie.owner.username
        searched_movie=''
        for each_user in self.users_collection:
            if each_user.username==username:
                user=each_user
        if user.username !=name_owner_of_movie:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for each_movie in user.movies_owned:
            if each_movie.title==movie.title:
                searched_movie=each_movie
        if searched_movie=='':
            raise Exception(f"The movie {movie.title} is not uploaded!")
        for each in user.movies_owned:
            if each.title==searched_movie.title:

                for key,value in kwargs.items(): # update the movie
                    setattr(each,key,value)

        return f"{username} successfully edited {movie.title} movie."


    def delete_movie(self,username: str, movie: Movie):
        user = ''
        name_owner_of_movie = movie.owner.username
        searched_movie = ''
        for each_user in self.users_collection:
            if each_user.username == username:
                user = each_user
        if user.username != name_owner_of_movie:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for each_movie in user.movies_owned:
            if each_movie.title==movie.title:
                searched_movie=each_movie
        if searched_movie=='':
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for each_movie in user.movies_owned:
            if each_movie.title==searched_movie.title:
                user.movies_owned.remove(each_movie)
        for each_movie in self.movies_collection:
            if each_movie.title==searched_movie.title:
                self.movies_collection.remove(each_movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self,username: str, movie: Movie):
        user = ''
        name_owner_of_movie = movie.owner.username
        searched_movie = ''
        for each_user in self.users_collection:
            if each_user.username == username:
                user = each_user
        if user.username == name_owner_of_movie:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        for each_movie in user.movies_liked:
            if each_movie.title==movie.title:
                searched_movie=each_movie
        if searched_movie!='':
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes+=1
        return f"{username} liked {movie.title} movie."


    def dislike_movie(self,username: str, movie: Movie):
        user = ''
        searched_movie = ''
        for each_user in self.users_collection:
            if each_user.username == username:
                user = each_user
        for each_movie in user.movies_liked:
            if each_movie.title == movie.title:
                searched_movie = each_movie
        if searched_movie == '':
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        """ have to be order by -year, then name !!!"""
        result=''
        for each in sorted(self.movies_collection,key= lambda x: (-x.year,x.title)):
            result+=f"{each.details()}"+'\n'
        return result.strip()


    def __str__(self):
        result=''
        if self.users_collection:
            result+=f"All users: {', '.join([x.username for x in self.users_collection])}"+'\n'
        else:
            result+="All users: No users."+'\n'
        if self.movies_collection:
            result+=f"All movies: {', '.join([x.title for x in self.movies_collection])}"
        else:
            result+="All movies: No movies."
        return  result

