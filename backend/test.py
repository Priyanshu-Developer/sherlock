import os
from dotenv import load_dotenv
import pymssql

load_dotenv()

# Database connection configuration
DB_CONFIG = {
    'server': os.getenv('DB_SERVER'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE')
}
ins =""

# Paste all your INSERT statements here as a string
insert_queries = """
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543210', 1, '2025-06-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543211', 2, '2025-06-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543212', 1, '2025-06-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543213', 3, '2025-06-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543214', 1, '2025-06-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543215', 2, '2025-06-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543216', 1, '2025-06-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543217', 4, '2025-06-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543218', 1, '2025-06-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543219', 2, '2025-06-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543220', 1, '2025-06-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543221', 3, '2025-06-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543222', 1, '2025-06-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543223', 2, '2025-06-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543224', 1, '2025-06-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543225', 4, '2025-06-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543226', 1, '2025-06-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543227', 2, '2025-06-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543228', 1, '2025-06-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543229', 3, '2025-06-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543230', 1, '2025-06-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543231', 2, '2025-06-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543232', 1, '2025-06-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543233', 4, '2025-06-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543234', 1, '2025-06-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543235', 2, '2025-06-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543236', 1, '2025-06-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543237', 3, '2025-06-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543238', 1, '2025-06-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543239', 2, '2025-06-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543240', 1, '2025-06-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543241', 4, '2025-06-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543242', 1, '2025-06-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543243', 2, '2025-06-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543244', 1, '2025-06-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543245', 3, '2025-06-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543246', 1, '2025-06-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543247', 2, '2025-06-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543248', 1, '2025-06-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543249', 4, '2025-06-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543250', 1, '2025-06-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543251', 2, '2025-06-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543252', 1, '2025-06-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543253', 3, '2025-06-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543254', 1, '2025-06-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543255', 2, '2025-06-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543256', 1, '2025-06-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543257', 4, '2025-06-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543258', 1, '2025-06-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543259', 2, '2025-06-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543260', 1, '2025-06-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543261', 3, '2025-06-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543262', 1, '2025-06-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543263', 2, '2025-06-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543264', 1, '2025-06-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543265', 4, '2025-06-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543266', 1, '2025-06-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543267', 2, '2025-06-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543268', 1, '2025-06-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543269', 3, '2025-06-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543270', 1, '2025-07-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543271', 2, '2025-07-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543272', 1, '2025-07-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543273', 4, '2025-07-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543274', 1, '2025-07-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543275', 2, '2025-07-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543276', 1, '2025-07-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543277', 3, '2025-07-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543278', 1, '2025-07-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543279', 2, '2025-07-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543280', 1, '2025-07-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543281', 4, '2025-07-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543282', 1, '2025-07-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543283', 2, '2025-07-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543284', 1, '2025-07-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543285', 3, '2025-07-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543286', 1, '2025-07-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543287', 2, '2025-07-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543288', 1, '2025-07-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543289', 4, '2025-07-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543290', 1, '2025-07-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543291', 2, '2025-07-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543292', 1, '2025-07-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543293', 3, '2025-07-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543294', 1, '2025-07-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543295', 2, '2025-07-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543296', 1, '2025-07-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543297', 4, '2025-07-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543298', 1, '2025-07-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543299', 2, '2025-07-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543300', 1, '2025-07-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543301', 3, '2025-07-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543302', 1, '2025-07-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543303', 2, '2025-07-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543304', 1, '2025-07-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543305', 4, '2025-07-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543306', 1, '2025-07-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543307', 2, '2025-07-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543308', 1, '2025-07-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543309', 3, '2025-07-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543310', 1, '2025-07-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543311', 2, '2025-07-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543312', 1, '2025-07-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543313', 4, '2025-07-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543314', 1, '2025-07-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543315', 2, '2025-07-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543316', 1, '2025-07-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543317', 3, '2025-07-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543318', 1, '2025-07-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543319', 2, '2025-07-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543320', 1, '2025-07-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543321', 4, '2025-07-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543322', 1, '2025-07-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543323', 2, '2025-07-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543324', 1, '2025-07-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543325', 3, '2025-07-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543326', 1, '2025-07-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543327', 2, '2025-07-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543328', 1, '2025-07-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543329', 4, '2025-07-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543330', 1, '2025-07-31');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543331', 2, '2025-07-31');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543332', 1, '2025-06-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543333', 1, '2025-06-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543334', 2, '2025-06-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543335', 1, '2025-06-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543336', 3, '2025-06-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543337', 1, '2025-06-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543338', 2, '2025-06-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543339', 1, '2025-06-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543340', 4, '2025-06-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543341', 1, '2025-06-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543342', 2, '2025-06-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543343', 1, '2025-06-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543344', 3, '2025-06-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543345', 1, '2025-06-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543346', 2, '2025-06-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543347', 1, '2025-06-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543348', 4, '2025-06-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543349', 1, '2025-06-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543350', 2, '2025-06-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543351', 1, '2025-06-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543352', 3, '2025-06-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543353', 1, '2025-06-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543354', 2, '2025-06-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543355', 1, '2025-06-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543356', 4, '2025-06-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543357', 1, '2025-06-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543358', 2, '2025-06-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543359', 1, '2025-06-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543360', 3, '2025-06-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543361', 1, '2025-06-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543362', 2, '2025-07-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543363', 1, '2025-07-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543364', 4, '2025-07-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543365', 1, '2025-07-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543366', 2, '2025-07-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543367', 1, '2025-07-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543368', 3, '2025-07-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543369', 1, '2025-07-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543370', 2, '2025-07-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543371', 1, '2025-07-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543372', 4, '2025-07-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543373', 1, '2025-07-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543374', 2, '2025-07-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543375', 1, '2025-07-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543376', 3, '2025-07-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543377', 1, '2025-07-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543378', 2, '2025-07-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543379', 1, '2025-07-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543380', 4, '2025-07-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543381', 1, '2025-07-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543382', 2, '2025-07-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543383', 1, '2025-07-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543384', 3, '2025-07-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543385', 1, '2025-07-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543386', 2, '2025-07-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543387', 1, '2025-07-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543388', 4, '2025-07-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543389', 1, '2025-07-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543390', 2, '2025-07-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543391', 1, '2025-07-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543392', 3, '2025-07-31');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543393', 1, '2025-06-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543394', 1, '2025-06-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543395', 1, '2025-06-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543396', 2, '2025-06-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543397', 1, '2025-06-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543398', 1, '2025-06-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543399', 3, '2025-06-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543400', 1, '2025-06-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543401', 1, '2025-06-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543402', 2, '2025-06-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543403', 1, '2025-06-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543404', 4, '2025-06-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543405', 1, '2025-06-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543406', 1, '2025-06-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543407', 2, '2025-06-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543408', 1, '2025-06-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543409', 3, '2025-06-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543410', 1, '2025-06-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543411', 1, '2025-06-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543412', 2, '2025-06-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543413', 1, '2025-06-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543414', 4, '2025-06-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543415', 1, '2025-06-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543416', 1, '2025-06-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543417', 2, '2025-06-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543418', 1, '2025-06-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543419', 3, '2025-06-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543420', 1, '2025-06-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543421', 1, '2025-06-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543422', 2, '2025-06-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543423', 1, '2025-07-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543424', 4, '2025-07-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543425', 1, '2025-07-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543426', 1, '2025-07-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543427', 2, '2025-07-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543428', 1, '2025-07-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543429', 3, '2025-07-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543430', 1, '2025-07-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543431', 1, '2025-07-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543432', 2, '2025-07-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543433', 1, '2025-07-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543434', 4, '2025-07-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543435', 1, '2025-07-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543436', 1, '2025-07-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543437', 2, '2025-07-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543438', 1, '2025-07-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543439', 3, '2025-07-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543440', 1, '2025-07-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543441', 1, '2025-07-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543442', 2, '2025-07-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543443', 1, '2025-07-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543444', 4, '2025-07-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543445', 1, '2025-07-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543446', 1, '2025-07-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543447', 2, '2025-07-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543448', 1, '2025-07-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543449', 3, '2025-07-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543450', 1, '2025-07-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543451', 1, '2025-07-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543452', 2, '2025-07-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543453', 1, '2025-07-31');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543454', 1, '2025-06-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543455', 2, '2025-06-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543456', 1, '2025-06-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543457', 3, '2025-06-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543458', 1, '2025-06-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543459', 2, '2025-06-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543460', 1, '2025-06-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543461', 4, '2025-06-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543462', 1, '2025-06-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543463', 2, '2025-06-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543464', 1, '2025-06-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543465', 3, '2025-06-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543466', 1, '2025-06-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543467', 2, '2025-06-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543468', 1, '2025-06-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543469', 4, '2025-06-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543470', 1, '2025-06-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543471', 2, '2025-06-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543472', 1, '2025-06-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543473', 3, '2025-06-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543474', 1, '2025-06-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543475', 2, '2025-06-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543476', 1, '2025-06-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543477', 4, '2025-06-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543478', 1, '2025-06-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543479', 2, '2025-06-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543480', 1, '2025-06-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543481', 3, '2025-06-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543482', 1, '2025-06-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543483', 2, '2025-06-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543484', 1, '2025-07-01');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543485', 4, '2025-07-02');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543486', 1, '2025-07-03');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543487', 2, '2025-07-04');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543488', 1, '2025-07-05');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543489', 3, '2025-07-06');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543490', 1, '2025-07-07');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543491', 2, '2025-07-08');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543492', 1, '2025-07-09');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543493', 4, '2025-07-10');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543494', 1, '2025-07-11');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543495', 2, '2025-07-12');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543496', 1, '2025-07-13');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543497', 3, '2025-07-14');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543498', 1, '2025-07-15');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543499', 2, '2025-07-16');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543500', 1, '2025-07-17');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543501', 4, '2025-07-18');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543502', 1, '2025-07-19');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543503', 2, '2025-07-20');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543504', 1, '2025-07-21');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543505', 3, '2025-07-22');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543506', 1, '2025-07-23');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543507', 2, '2025-07-24');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543508', 1, '2025-07-25');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543509', 4, '2025-07-26');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543510', 1, '2025-07-27');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543511', 2, '2025-07-28');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543512', 1, '2025-07-29');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543513', 3, '2025-07-30');
INSERT INTO Wafunnel (Number, Stage, Date) VALUES ('+919876543514', 1, '2025-07-31');
"""

def run_insert_queries(queries: str):
    try:
        conn = pymssql.connect(
            server=DB_CONFIG['server'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
        )
        cursor = conn.cursor()
        
        # Split the queries and execute one by one
        for query in queries.strip().split(';'):
            clean_query = query.strip()
            if clean_query:  # Avoid empty lines
                cursor.execute(clean_query)

        conn.commit()
        print("✅ All queries executed successfully!")

    except Exception as e:
        print("❌ Error executing queries:", e)

    finally:
        if conn:
            conn.close()

# Run it
run_insert_queries(insert_queries)
