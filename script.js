/**
 * Write a constructor for making “Book” objects.
 * We will revisit this in the project at the end of this lesson. 
 * Your book objects should have the book’s title, author, the number of pages, and whether or not you have read the book.
 */

function Book (title, author, numOfPages, status){
    this.title = title;
    this.author = author;
    this.numOfPages = numOfPages;
    this.status = status;

    this.info = function(){
        let summary = `${this.title} by ${this.author}, ${this.numOfPages} pages, ${status}`;
        return summary;
    }

   
}

const first = new Book("Journey to South", "Blama Doe", 23, "read completely");
console.log(first.info())