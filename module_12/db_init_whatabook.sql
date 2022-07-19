DROP USER IF EXISTS 'whatabook_user'@'localhost';


CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;


CREATE TABLE user (
    user_id         INT                 NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75)         NOT NULL,
    last_name       VARCHAR(75)         NOT NULL,
    PRIMARY KEY(user_id) 
);


CREATE TABLE book (
    book_id             INT             NOT NULL        AUTO_INCREMENT,
    book_name           VARCHAR(200)    NOT NULL,
    details             VARCHAR(500),
    author              VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);


CREATE TABLE store (
    store_id            INT             NOT NULL        AUTO_INCREMENT,
    locale              VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT                 NOT NULL    AUTO_INCREMENT,
    user_id         INT                 NOT NULL,
    book_id         INT                 NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

INSERT INTO store(locale)
    VALUES ('123 Main Street, Papillion, NE 68046');

INSERT INTO book(book_name, author, details)
    VALUES('One Hundred Years of Solitude','Gabriel Garcia Marquez','Released in 1982');

INSERT INTO book(book_name, author, details)
    VALUES('To Kill A Mockingbird', 'Harper Lee', "Pulizter Prize winning American Classic");

INSERT INTO book(book_name, author, details)
    VALUES('1984', 'George Orwell', 'Released in 1949');

INSERT INTO book(book_name, author, details)
    VALUES('The Great Gatsby', 'F. Scott Fitzerland',"Set in the 1920s in New York City");

INSERT INTO book(book_name, author, details)
    VALUES('The Old Mand and the Sea', 'Ernest Hemingway', 'Nobel Prize winner for Literature');

INSERT INTO book(book_name, author, details)
    VALUES('A Brief History of Time: From Big Bang to Black Holes', 'Stephen Hawking','Classic book that explains what created the universe');

INSERT INTO book(book_name, author, details)
    VALUES('The Intelligent Investor', 'Benjamin Graham','Beginners Guide to Investing');

INSERT INTO book(book_name, author, details)
    VALUES('Adventures of Huckleberry Finn', 'Mark Twain','Known as the Great American Novel');

INSERT INTO book(book_name, author, details)
    VALUES('The Adventures of Sherlock Holmes', 'Arthur Conan Doyle', 'Classic detective novel');

INSERT INTO book(book_name, author, details)
    VALUES('Animal Farm', 'George Orwell', 'Allegorical book that mirrors the Russian Revolution of 1917');

INSERT INTO book(book_name, author, details)
    VALUES('The Catcher in the Rye','J.D. Salinger','Book about the meaning of youth');

INSERT INTO user(first_name, last_name)
    VALUES('Bill', 'Jones');

INSERT INTO user(first_name, last_name)
    VALUES('Nate', 'Thomas');

INSERT INTO user(first_name, last_name)
    VALUES('Becca', 'Smith');


INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Bill'),
        (SELECT book_id FROM book WHERE book_name = 'Animal Farm')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Nate'),
        (SELECT book_id FROM book WHERE book_name = 'The Intelligent Investor')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Becca'),
        (SELECT book_id FROM book WHERE book_name = 'The Catcher in the Rye')
    );