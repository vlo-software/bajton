import { IArticle } from "@/interfaces/db/article";
import { baseRepo } from "./baseRepo";

export class articleRepo extends baseRepo {
  constructor() {
    super();
  }

  async getById(id: number): Promise<IArticle | null> {
    const article = await this.prisma.article.findUnique({ where: { id: id } });
    return article ? (article as IArticle) : null;
  }

  async getByOwnerId(ownerId: number): Promise<IArticle[] | null> {
    const articles = await this.prisma.article.findMany({
      where: { ownerId: ownerId },
    });
    return articles ? (articles as IArticle[]) : null;
  }

  async add(newArticle: IArticle): Promise<void> {
    await this.prisma.article.create({ data: newArticle });
  }

  async update(articleToUpdate: Partial<IArticle>): Promise<void> {
    await this.prisma.article.update({
      where: { id: articleToUpdate._id },
      data: articleToUpdate,
    });
  }

  async delete(id: number): Promise<void> {
    await this.prisma.article.delete({ where: { id: id } });
  }
}
